# Co Coder 🤖

Co Coder is an autonomous AI developer agent built by **Otic Technologies**. It is designed to perform file operations safely and efficiently within a local development workspace.

### Features
* **Autonomous File Operations:** Create, read, and update files using natural language.
* **Secure Sandbox:** Operations are contained within a `/workspace` directory to protect your core system.
* **Local Control:** Open-source and developer-focused.

## Setup Instructions

### 1. Requirements
* Python 3.x
* NVIDIA API Key (Get one at [build.nvidia.com](https://build.nvidia.com/))

### 2. Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/co-coder.git](https://github.com/YOUR_USERNAME/co-coder.git)
   cd co-coder

##
   # Create and activate your environment:
1. python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

2. Create your config.py:
    Copy config.example.py to config.py.

    Add your NVIDIA API Key:

    Python
    API_KEY = "nvapi-xxxxxxxxxxxxxxxxxxxxxxxxxxxx"   
### Usage
* Launch the agent:

Bash
python main.py 
* Enter your prompts at the terminal interface.

### Contact
* Development team: frenchkaptain@gmail.com