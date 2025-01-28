import argparse
from controller import TaskController

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("description", type=str, help="New task description")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Mark a task as in-progress")
    mark_in_progress_parser.add_argument("id", type=int, help="Task ID")

    mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
    mark_done_parser.add_argument("id", type=int, help="Task ID")

    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("status", type=str, nargs="?", choices=["done", "todo", "in-progress"], help="Filter by task status")

    args = parser.parse_args()
    controller = TaskController()

    if args.command == "add":
        controller.add_task(args.description)
    elif args.command == "update":
        controller.update_task(args.id, args.description)
    elif args.command == "delete":
        controller.delete_task(args.id)
    elif args.command == "mark-in-progress":
        controller.mark_in_progress(args.id)
    elif args.command == "mark-done":
        controller.mark_done(args.id)
    elif args.command == "list":
        controller.list_tasks(args.status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
