import engine

def main():
    print("===============================================================")
    print("MODULAR RUNTIME ACTIVE")
    print("===============================================================")
    print("Commands: Type 'exit' or 'quit' to close down operations.")
    
    while True:
        user_input = input("\nUser Prompt: ").strip()
        
        if user_input.lower() in ['exit', 'quit']:
            print("Shutting down operations.")
            break
            
        if not user_input:
            continue
            
        engine.run_agent_loop(user_input)

if __name__ == "__main__":
    main()