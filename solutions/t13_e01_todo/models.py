from dataclasses import dataclass


PRIORITIES = ("high", "medium", "low")


@dataclass
class Task:
    id: int
    title: str
    priority: str = "medium"
    done: bool = False


class TodoList:
    def __init__(self, tasks=None):
        self.tasks = list(tasks) if tasks is not None else []
        self._next_id = max((task.id for task in self.tasks), default=0) + 1

    def add_task(self, title, priority="medium"):
        priority = priority.lower()
        if priority not in PRIORITIES:
            raise ValueError("priority must be high, medium or low")

        task = Task(self._next_id, title, priority)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self):
        priority_order = {priority: index for index, priority in enumerate(PRIORITIES)}
        return sorted(
            self.tasks,
            key=lambda task: (task.done, priority_order[task.priority], task.id),
        )

    def complete_task(self, task_id):
        task = self._find_task(task_id)
        task.done = True
        return task

    def delete_task(self, task_id):
        task = self._find_task(task_id)
        self.tasks.remove(task)
        return task

    def _find_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"no task with id {task_id}")
