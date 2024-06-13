import pytest
from utils import run_task_command

def test_annotate_task():
    run_task_command('task add "Leetcode Test Preparation" due:eow')
    run_task_command('task 10 annotate "Focus on Algorithms"')
    stdout, _ = run_task_command('task 10 info')
    assert "Focus on Algorithms" in stdout
    print(stdout)
