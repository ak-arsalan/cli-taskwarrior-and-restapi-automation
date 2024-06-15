def test_delete_task(run_task_command):
    run_task_command('task add "Task to be deleted" due:today')
    stdout, _ = run_task_command('task list')
    lines = stdout.splitlines()
    task_ids = []
    for line in lines:
        columns = line.split()
        if columns and columns[0].isdigit():
            task_ids.append(columns[0])
    for task_id in task_ids:
        run_task_command(f'task {task_id} rc.confirmation=no rc.bulk=0 delete')
    stdout, _ = run_task_command('task list')
    assert "Task to be deleted" not in stdout

