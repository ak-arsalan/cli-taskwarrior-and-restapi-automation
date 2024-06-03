import subprocess
import pytest

def run_task_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command '{command}': {result.stderr}")
    return result.stdout.strip(), result.stderr.strip()

def test_complete_task():
    run_task_command('task add "Rasa Given Task Done" due:today')
    stdout, _ = run_task_command('task list')
    print(run_task_command('task list'))
    run_task_command('task 3 done')
    stdout, _ = run_task_command('task completed')
    assert "Rasa Given Task Done" in stdout

