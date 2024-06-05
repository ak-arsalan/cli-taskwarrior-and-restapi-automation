import subprocess
import pytest

def run_task_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command '{command}': {result.stderr}")
    return result.stdout.strip(), result.stderr.strip()

def test_add_task_with_annotation():
    run_task_command('task add "Research Berlin Places to Visit" due:tomorrow')
    run_task_command('task 5 annotate "Visit Brandenburg Gate and Museum Island"')
    stdout, _ = run_task_command('task 5 info')
    assert "Visit Brandenburg Gate and Museum Island" in stdout
