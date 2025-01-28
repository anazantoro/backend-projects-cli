class TaskView:
    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_tasks(tasks):
        if not tasks:
            print("No tasks found.")
        for task in tasks:
            print(f"[{task['status'].upper()}] ID: {task['id']} - {task['description']} (Created: {task['createdAt']}, Updated: {task['updatedAt']})")
