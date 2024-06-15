import subprocess
import pytest

BASE_URL = "https://fakestoreapi.com"

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def run_task_command():
    def _run_task_command(command):
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running command '{command}': {result.stderr}")
        return result.stdout.strip(), result.stderr.strip()

    return _run_task_command

def cleanup_tasks(run_task_command):
    """Function to list all tasks and delete them."""
    stdout, _ = run_task_command('task list')
    lines = stdout.splitlines()
    task_ids = []
    for line in lines:
        columns = line.split()
        if columns and columns[0].isdigit():
            task_ids.append(columns[0])
    for task_id in task_ids:
        run_task_command(f'task {task_id} rc.confirmation=no rc.bulk=0 delete')

@pytest.fixture(autouse=True)
def run_before_and_after_tests(run_task_command):
    """Fixture to run cleanup before and after each test."""
    cleanup_tasks(run_task_command)
    yield
    cleanup_tasks(run_task_command)
