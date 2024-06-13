import pytest
from utils import run_task_command

def test_append_task():
    run_task_command("task add fix the window")
    run_task_command("task 1 append before the storm comes project:Home +repair")
    stdout, _ = run_task_command('task 11 info')
    assert "fix the window before the storm comes"
    print(stdout)
