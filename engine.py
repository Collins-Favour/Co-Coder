import sys
import re
from openai import OpenAI
import config
import tools

client = OpenAI(base_url=config.BASE_URL, api_key=config.NVIDIA_API_KEY)

SYSTEM_PROMPT = """You are an advanced software engineering agent. 
You can view and modify local codebase structures using these explicit structural tags:

1. List folder files: [TOOL:LIST_FILES]
2. Read a file's code: [TOOL:READ_FILE path="filename.ext"]
3. Save/Update a file: 
[TOOL:WRITE_FILE path="filename.ext"]
CODE_CONTENT
[/TOOL:WRITE_FILE]

Always explicitly output your structural commands when performing operations. Output only ONE tool instruction per response turn.
"""

def parse_and_execute(text_payload):
    """Scans response text for tool tags and executes the Python file tools."""
    if "[TOOL:LIST_FILES]" in text_payload:
        print(f"\n{config.COLOR_TOOL}[Executing: Listing local files...]{config.COLOR_RESET}")
        return tools.list_workspace()
        
    if '[TOOL:READ_FILE path="' in text_payload:
        match = re.search(r'path="([^"]+)"', text_payload)
        if match:
            filepath = match.group(1)
            print(f"\n{config.COLOR_TOOL}[Executing: Reading content from {filepath}...]{config.COLOR_RESET}")
            return tools.read_target_file(filepath)
            
    if '[TOOL:WRITE_FILE path="' in text_payload:
        match_path = re.search(r'path="([^"]+)"', text_payload)
        if match_path:
            filepath = match_path.group(1)
            start_tag = text_payload.find(']') + 1
            end_tag = text_payload.find('[/TOOL:WRITE_FILE]')
            content = text_payload[start_tag:end_tag].replace(f'[TOOL:WRITE_FILE path="{filepath}"]', "").strip()
            
            print(f"\n{config.COLOR_TOOL}[Executing: Writing structural file: {filepath}...]{config.COLOR_RESET}")
            return tools.write_target_file(filepath, content)
            
    return None

def run_agent_loop(user_instruction):
    conversation_history = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_instruction}
    ]
    
    for loop_hop in range(4):
        print(f"\n[System]: Handoff to Llama 3.3 via Nvidia (Turn {loop_hop + 1})...")
        
        try:
            completion = client.chat.completions.create(
                model=config.MODEL_NAME,
                messages=conversation_history,
                temperature=0.2, 
                top_p=0.7,
                max_tokens=2048,
                stream=True
            )
            
            accumulated_content = ""
            printing_content = False
            
            for chunk in completion:
                if not chunk.choices:
                    continue
                content = chunk.choices[0].delta.content
                if content is not None:
                    if not printing_content:
                        print(f"\n{config.COLOR_AGENT}[Agent Response]:\n", end="")
                        printing_content = True
                    print(content, end="")
                    sys.stdout.flush()
                    accumulated_content += content

            print(config.COLOR_RESET)
            
            tool_feedback = parse_and_execute(accumulated_content)
            
            if tool_feedback:
                conversation_history.append({"role": "assistant", "content": accumulated_content})
                conversation_history.append({"role": "user", "content": f"TOOL OUTCOME:\n{tool_feedback}"})
            else:
                print("\n[System]: Task completed cleanly.")
                break
                
        except Exception as e:
            print(f"\n[Error]: Execution Encountered: {str(e)}")
            break