class TaskService:
    def __init__(self, repository):
        self.repo = repository

    def add_task(self, title, description):
        if not title.strip():
            raise ValueError("Title cannot be empty")
        return self.repo.add_task(title, description)

    def delete_task(self, task_id: int):
        if not self.repo.delete_task(task_id):
            raise ValueError("Task not found")

