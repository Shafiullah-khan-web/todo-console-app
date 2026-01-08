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

    def toggle_complete(self, task_id: int):
        task = self.repo.toggle_complete(task_id)
        if not task:
            raise ValueError("Task not found")
        return task

    def update_task(self, task_id: int, title: str, description: str):
        task = self.repo.update_task(task_id, title, description)
        if not task:
            raise ValueError("Task not found")
        return task

