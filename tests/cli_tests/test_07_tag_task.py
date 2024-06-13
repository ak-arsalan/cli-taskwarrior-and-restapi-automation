import pytest
from utils import run_task_command

def test_tag_task():
    run_task_command('task add "Plan Munich Tour in next month Vacation" due:eom')
    run_task_command('task 6 modify +Vacation +Planning')
    stdout, _ = run_task_command('task 6 info')
    assert "Vacation" in stdout
    assert "Planning" in stdout
    print(stdout)
