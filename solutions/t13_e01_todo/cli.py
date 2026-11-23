import argparse

from .models import TodoList
from .storage import load, save


MENU = "1) Add task  2) List tasks  3) Complete task  4) Delete task  5) Quit"


def _read_task_id():
    raw_id = input("Task id: ").strip()
    try:
        return int(raw_id)
    except ValueError:
        print(f"'{raw_id}' is not a number.")
        return None


def main(argv=None):
    parser = argparse.ArgumentParser(description="Manage a to-do list.")
    parser.add_argument("--file", default="todo.json", help="JSON file for saved tasks")
    args = parser.parse_args(argv)

    tasks = load(args.file)
    todo = TodoList(tasks)
    print(f"Loaded {len(todo.tasks)} task(s) from {args.file}")

    try:
        while True:
            print(f"\n{MENU}")
            choice = input("Choice: ").strip()

            if choice == "1":
                title = input("Title: ").strip()
                priority = input("Priority (high/medium/low) [medium]: ").strip()
                if not priority:
                    priority = "medium"
                try:
                    task = todo.add_task(title, priority)
                except ValueError as error:
                    print(f"Error: {error}")
                    continue
                save(args.file, todo.tasks)
                print(f"Added task {task.id}.")
            elif choice == "2":
                for task in todo.list_tasks():
                    marker = "x" if task.done else " "
                    print(f"[{marker}]  {task.id}. {task.title} ({task.priority})")
                open_count = sum(not task.done for task in todo.tasks)
                done_count = len(todo.tasks) - open_count
                print(f"{open_count} open, {done_count} done")
            elif choice in ("3", "4"):
                task_id = _read_task_id()
                if task_id is None:
                    continue
                try:
                    if choice == "3":
                        task = todo.complete_task(task_id)
                        save(args.file, todo.tasks)
                        print(f"Completed: {task.title}")
                    else:
                        task = todo.delete_task(task_id)
                        save(args.file, todo.tasks)
                        print(f"Deleted: {task.title}")
                except ValueError as error:
                    print(f"Error: {error}")
            elif choice == "5":
                break
            else:
                print("Please choose 1-5.")
    except EOFError:
        pass

    save(args.file, todo.tasks)
    print(f"Saved {len(todo.tasks)} task(s). Bye.")
    return 0
