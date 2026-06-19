import os

import os

BASE_DIR = 'workspace'

def list_workspace():
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
    files = [f for f in os.listdir(BASE_DIR)]
    return "\n".join(files) if files else "Workspace is empty."



def read_target_file(filepath):
    """Reads the contents of a local file."""
    try:
        if not os.path.exists(filepath):
            return f"Error: The file '{filepath}' does not exist."
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file '{filepath}': {str(e)}"

def write_target_file(filepath, content):
    """Writes or updates a file."""
    try:
        clean_content = content.replace('[/TOOL:WRITE_FILE]', '').strip()
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(clean_content)
        return f"Success: File '{filepath}' has been written to the workspace."
    except Exception as e:
        return f"Error writing to file '{filepath}': {str(e)}"