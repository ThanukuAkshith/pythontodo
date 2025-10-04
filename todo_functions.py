from tasks import tasks

def save_tasks(tasks):
    with open("tasks.py", "w") as file:
        file.write("tasks = [\n")
        for task in tasks:
            file.write(f" {{'id': {task['id']}, 'task': '{task['task']}', 'status': '{task['status']}' }},\n")
        file.write("]\n\nmax_tasks = 8")

def add_task(tasks, max_tasks):
    if len(tasks) >= max_tasks:
        print("Cannot add more than 8 tasks!")
        return
    task_description = input("Enter the task you want to add: ")
    task_id = tasks[-1]["id"] + 1 if tasks else 1
    tasks.append({"id": task_id, "task": task_description, "status": "Pending"})
    save_tasks(tasks)
    print(f"Task added with ID {task_id}!")

def view_task(tasks):
    if not tasks:
        print("No tasks available!")
        return
    print("\n-------- Your Tasks --------")
    for task in tasks:
        print(f"ID: {task['id']} | Task: {task['task']} | Status: {task['status']}")

def update_task(tasks):
    task_id = int(input("Enter Task ID to update: "))
    for task in tasks:
        if task["id"] == task_id:
            new_desc = input("Enter new description: ")
            task["task"] = new_desc
            save_tasks(tasks)
            print("Task updated successfully!")
            return
    print("Task not found!")

def mark_done(tasks):
    task_id = int(input("Enter Task ID to mark as done: "))
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Done"
            save_tasks(tasks)
            print("Task marked as done!")
            return
    print("Task not found!")

def delete_task(tasks):
    task_id = int(input("Enter Task ID to delete: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!")
            return
    print("Task not found!")
