import subprocess

def run_task_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command '{command}': {result.stderr}")
    return result.stdout.strip(), result.stderr.strip()