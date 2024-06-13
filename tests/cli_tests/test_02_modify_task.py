import pytest
from utils import run_task_command

def test_modify_task():
    run_task_command('task add "Welcome to the Team" due:today')
    run_task_command('task 2 modify description:"Welcome to the Team Arsalan" due:tomorrow')
    stdout, _ = run_task_command('task 2 info')
    assert "Welcome to the Team Arsalan" in stdout
    print(stdout)
