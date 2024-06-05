import subprocess
import pytest

def run_task_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command '{command}': {result.stderr}")
    return result.stdout.strip(), result.stderr.strip()

def test_tag_task():
    run_task_command('task add "Plan Munich Tour in next month Vacation" due:eom')
    run_task_command('task 6 modify +Vacation +Planning')
    stdout, _ = run_task_command('task 6 info')
    assert "Vacation" in stdout
    assert "Planning" in stdout
