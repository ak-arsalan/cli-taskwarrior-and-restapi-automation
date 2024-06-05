import subprocess
import pytest

def run_task_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command '{command}': {result.stderr}")
    return result.stdout.strip(), result.stderr.strip()

def test_search_tasks_by_tags():
    run_task_command('task add "Go for Grocery From Rewe Store" +Grocery')
    run_task_command('task add "Library Visit" +Studying')
    stdout, _ = run_task_command('task +Grocery list')
    assert "Grocery From Rewe" in stdout
    assert "Library Visit" not in stdout
