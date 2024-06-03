import subprocess
import pytest

def run_task_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command '{command}': {result.stderr}")
    return result.stdout.strip(), result.stderr.strip()

def test_modify_task():
    run_task_command('task add "Welcome to Rasa" due:today')
    run_task_command('task 2 modify description:"Welcome to Rasa Arsalan" due:tomorrow')
    stdout, _ = run_task_command('task 2 info')
    assert "Welcome to Rasa Arsalan" in stdout
