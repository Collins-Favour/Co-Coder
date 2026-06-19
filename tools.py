import os

def list_workspace():
    """Lists all files in the current folder."""
    try:
        files = [f for f in os.listdir('.') if not f.startswith('.') and not f.startswith('__')]
        if not files:
            return "The workspace directory is currently empty."
        return "\n".join(files)
    except Exception as e:
        return f"Error scanning directory: {str(e)}"

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