def test_search_tasks_by_tags(run_task_command):
    run_task_command('task add "Go for Grocery From Rewe Store" +Grocery')
    run_task_command('task add "Library Visit" +Studying')
    stdout, _ = run_task_command('task +Grocery list')
    assert "Grocery From Rewe" in stdout
    assert "Library Visit" not in stdout
