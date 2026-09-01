from app import add_task, view_tasks, complete_task, delete_task, tasks


def setup_function():
    tasks.clear()


def test_add_task():
    add_task("Complete Python assignment")
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Complete Python assignment"


def test_complete_task():
    add_task("Study DevOps")
    assert complete_task(0) is True
    assert tasks[0]["completed"] is True


def test_delete_task():
    add_task("Submit project")
    assert delete_task(0) is True
    assert len(tasks) == 0


def test_invalid_task_index():
    assert complete_task(10) is False