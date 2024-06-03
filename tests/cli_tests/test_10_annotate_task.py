import subprocess
import pytest

def run_task_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command '{command}': {result.stderr}")
    return result.stdout.strip(), result.stderr.strip()

def test_annotate_task():
    run_task_command('task add "Leetcode Test" due:eow')
    run_task_command('task 10 annotate "Focus on Algorithms"')
    stdout, _ = run_task_command('task 10 info')
    assert "Focus on Algorithms" in stdout
