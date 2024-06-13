import pytest
from utils import run_task_command

def test_list_tasks_by_due_date():
    run_task_command('task add "Task 1" due:2024-06-05')
    run_task_command('task add "Task 2" due:2024-06-06')
    run_task_command('task add "Task 3" due:2024-06-07')
    stdout, _ = run_task_command('task list due')
    assert "Task 1" in stdout
    assert "Task 2" in stdout
    assert "Task 3" in stdout
    print(stdout)
