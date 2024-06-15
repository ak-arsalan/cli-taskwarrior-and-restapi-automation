def test_recurring_task(run_task_command):
    run_task_command('task add "Join Berlin Events every month" due:tomorrow recur:weekly')
    stdout, _ = run_task_command('task list')
    assert "Join Berlin Events every month" in stdout
