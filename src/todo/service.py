class TaskService:
    def __init__(self, repository):
        self.repo = repository

    def add_task(self, title, description):
        if not title.strip():
            raise ValueError("Title cannot be empty")
        return self.repo.add_task(title, description)

