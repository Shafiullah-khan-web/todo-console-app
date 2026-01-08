class TodoCLI:
    def __init__(self, service):
        self.service = service

    def add(self):
        title = input("Title: ")
        description = input("Description: ")
        task = self.service.add_task(title, description)
        print(f"Task added (ID: {task.id})")

    def list_tasks(self):
        tasks = self.service.repo.get_all()
        if not tasks:
            print("No tasks found.")
            return

        for task in tasks:
            status = "✓" if task.completed else " "
            print(f"[{status}] {task.id}. {task.title}")

    def delete(self, task_id: int):
        try:
            self.service.delete_task(task_id)
            print(f"Task {task_id} deleted successfully")
        except ValueError as e:
            print(e)

    def complete(self, task_id: int):
        try:
            task = self.service.toggle_complete(task_id)
            status = "complete" if task.completed else "incomplete"
            print(f"Task {task_id} marked as {status}")
        except ValueError as e:
            print(e)

    def update(self, task_id: int):
        title = input("New title: ")
        description = input("New description: ")
        try:
            self.service.update_task(task_id, title, description)
            print(f"Task {task_id} updated")
        except ValueError as e:
            print(e)

