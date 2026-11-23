class Queue:
    def __init__(self):
        self._inbox = []
        self._outbox = []

    def enqueue(self, item):
        self._inbox.append(item)

    def _fill_outbox(self):
        if not self._outbox:
            while self._inbox:
                self._outbox.append(self._inbox.pop())

    def dequeue(self):
        self._fill_outbox()
        if not self._outbox:
            raise IndexError("dequeue from empty queue")
        return self._outbox.pop()

    def front(self):
        self._fill_outbox()
        if not self._outbox:
            raise IndexError("front from empty queue")
        return self._outbox[-1]

    def is_empty(self):
        return not self._inbox and not self._outbox

    def __len__(self):
        return len(self._inbox) + len(self._outbox)


def process_jobs(jobs):
    queue = Queue()
    for job in jobs:
        queue.enqueue(job)

    processed = []
    while not queue.is_empty():
        processed.append(queue.dequeue())
    return processed


q = Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
print("front:", q.front())
print("dequeue:", q.dequeue())
q.enqueue("d")
print("size:", len(q))
print("remaining:", [q.dequeue() for _ in range(len(q))])
print("jobs:", process_jobs(["report.pdf", "photo.png", "notes.txt"]))