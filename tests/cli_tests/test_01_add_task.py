import pytest
from utils import run_task_command

def test_add_task():
    run_task_command('task add "Submission of Assignment" due:tomorrow')
    stdout, _ = run_task_command('task list')
    assert "Submission of Assignment" in stdout
    print(stdout)
