def test_complete_task(run_task_command):
    run_task_command('task add "Given Task Done" due:today')
    run_task_command("task list")
    run_task_command('task 1 done')
    stdout, _ = run_task_command('task completed')
    assert "Given Task Done" in stdout

