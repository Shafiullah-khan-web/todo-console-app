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

