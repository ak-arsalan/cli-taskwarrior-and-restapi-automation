import subprocess
import pytest

def run_task_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command '{command}': {result.stderr}")
    return result.stdout.strip(), result.stderr.strip()

def test_modify_task():
    run_task_command('task add "Welcome to the Team" due:today')
    run_task_command('task 2 modify description:"Welcome to the Team Arsalan" due:tomorrow')
    stdout, _ = run_task_command('task 2 info')
    assert "Welcome to the Team Arsalan" in stdout
