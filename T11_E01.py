class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


def is_balanced(text):
    stack = Stack()
    opening = "([{"
    matching_opening = {")": "(", "]": "[", "}": "{"}

    for character in text:
        if character in opening:
            stack.push(character)
        elif character in matching_opening:
            if stack.is_empty() or stack.pop() != matching_opening[character]:
                return False

    return stack.is_empty()


s = Stack()
for n in [10, 20, 30]:
    s.push(n)
print("size:", len(s))
print("peek:", s.peek())
print("pop:", s.pop())
print("size after pop:", len(s))
for text in ["(a + b) * [c]", "{[()]}", "(]", "((x)"]:
    print(f"{text!r} balanced: {is_balanced(text)}")