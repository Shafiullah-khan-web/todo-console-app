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

    def delete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False

    def toggle_complete(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = not task.completed
                return task
        return None

    def update_task(self, task_id: int, title: str, description: str):
        for task in self.tasks:
            if task.id == task_id:
                task.title = title
                task.description = description
                return task
        return None

