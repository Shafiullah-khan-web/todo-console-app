from typing import List, Optional
from .models import Task

class TaskRepository:
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, title: str, description: str) -> Task:
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all(self):
        return self.tasks

