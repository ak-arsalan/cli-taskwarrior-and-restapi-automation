import pytest
from utils import run_task_command

def test_add_task_with_annotation():
    run_task_command('task add "Research Berlin Places to Visit" due:tomorrow')
    run_task_command('task 5 annotate "Visit Brandenburg Gate and Museum Island"')
    stdout, _ = run_task_command('task 5 info')
    assert "Visit Brandenburg Gate and Museum Island" in stdout
    print(stdout)
