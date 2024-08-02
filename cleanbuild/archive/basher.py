# basher.py

import subprocess

def run_bash_command(command):
    """
    Runs a bash command and returns the output or error message.

    Parameters:
    command (str): The bash command to run.

    Returns:
    str: The output or error message from running the command.
    """
    try:
        # Run the command and get the output
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Return the output
        return result.stdout.strip()
        
    except subprocess.CalledProcessError as e:
        # Return the error message
        return f"Command failed with exit code {e.returncode}\nError output:\n{e.stderr.strip()}"
