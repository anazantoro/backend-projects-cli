import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

class TaskModel:
    def __init__(self):
        if not os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "w") as file:
                json.dump([], file)

    def load_tasks(self):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)

    def save_tasks(self, tasks):
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=4)

    def generate_id(self):
        tasks = self.load_tasks()
        return max([task["id"] for task in tasks], default=0) + 1

    def add_task(self, description):
        tasks = self.load_tasks()
        task = {
            "id": self.generate_id(),
            "description": description,
            "status": "todo",
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat(),
        }
        tasks.append(task)
        self.save_tasks(tasks)
        return task
