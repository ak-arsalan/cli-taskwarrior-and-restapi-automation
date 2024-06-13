import pytest
from utils import run_task_command

def test_complete_task():
    run_task_command('task add "Given Task Done" due:today')
    stdout, _ = run_task_command('task list')
    run_task_command('task 3 done')
    stdout, _ = run_task_command('task completed')
    assert "Given Task Done" in stdout
    print(stdout)

