import subprocess
import pytest

def run_task_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command '{command}': {result.stderr}")
    return result.stdout.strip(), result.stderr.strip()

def test_delete_task():
    run_task_command('task add "Welcome to Rasa" due:today')
    run_task_command('task 4 rc.confirmation=no rc.bulk=0 delete')
    stdout, _ = run_task_command('task list')
    assert "Submittion of Assignment to Rasa" not in stdout

