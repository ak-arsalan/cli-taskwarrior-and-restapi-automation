def test_annotate_task(run_task_command):
    run_task_command('task add "Leetcode Test Preparation" due:eow')
    run_task_command('task 1 annotate "Focus on Algorithms"')
    stdout, _ = run_task_command('task 1 info')
    assert "Focus on Algorithms" in stdout
