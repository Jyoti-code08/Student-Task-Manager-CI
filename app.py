tasks = []


def add_task(task):
    tasks.append({"task": task, "completed": False})


def view_tasks():
    return tasks


def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        return True
    return False


def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        return True
    return False


if __name__ == "__main__":
    print("Student Task Manager")