import subprocess
import pytest

def run_task_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command '{command}': {result.stderr}")
    return result.stdout.strip(), result.stderr.strip()
    
def test_recurring_task():
    run_task_command('task add "Outing with Wife" due:tomorrow recur:weekly')
    stdout, _ = run_task_command('task list')
    assert "Outing with Wife" in stdout