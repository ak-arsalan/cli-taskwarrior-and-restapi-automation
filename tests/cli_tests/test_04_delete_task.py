import pytest
from utils import run_task_command

def test_delete_task():
    run_task_command('task add "Task to be deleted" due:today')
    run_task_command('task 3 rc.confirmation=no rc.bulk=0 delete')
    stdout, _ = run_task_command('task list')
    assert "Task to be deleted" not in stdout
    print(stdout)

