# Mimi Mini Project

A tiny Python CLI to manage tasks for Mimi.

## What it does:
- Reads tasks.yaml and lists tasks
- Can run a task by name (echo, time, shell)
- Simple CLI using argparse

## Setup & Run

**Prerequisites:**
- Python 3.x
- pip

**Steps:**

1.  **Navigate to the project directory:**
    ```bash
    cd /home/donald_gor113/.openclaw/workspace/mimi-mini-project
    ```

2.  **Install dependencies:**
    ```bash
    pip3 install pyyaml
    ```

3.  **Make the script executable (optional):**
    ```bash
    chmod +x main.py
    ```

4.  **List available tasks:**
    ```bash
    python3 main.py list
    ```
    *Expected output:*
    ```
    - docs: Documentation — Simple project config
    ```

5.  **Run a specific task:**
    ```bash
    python3 main.py run docs
    ```
    *Expected output:*
    ```
    Hello from Mimi mini-project
    ```

**Verification:**
- Ensure the command returns exit code 0.
- Check the console output for the expected message such as "Hello from Mimi mini-project".

Feel free to add more tasks to `tasks.yaml` and run them!