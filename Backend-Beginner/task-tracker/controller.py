from model import TaskModel
from view import TaskView
from datetime import datetime

class TaskController:
    def __init__(self):
        self.model = TaskModel()
        self.view = TaskView()

    def add_task(self, description):
        task = self.model.add_task(description)
        self.view.display_message(f"Task added successfully (ID: {task['id']})")

    def list_tasks(self, status=None):
        tasks = self.model.load_tasks()
        if status:
            tasks = [task for task in tasks if task["status"] == status]
        self.view.display_tasks(tasks)

    def update_task(self, task_id, description):
        tasks = self.model.load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["description"] = description
                task["updatedAt"] = datetime.now().isoformat()
                self.model.save_tasks(tasks)
                self.view.display_message("Task updated successfully")
                return
        self.view.display_message(f"Task with ID {task_id} not found")
