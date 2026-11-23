def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


OPERATIONS = {
    "add": add,
    "sub": sub,
    "mul": mul,
}


def calculate(op_name, a, b):
    try:
        operation = OPERATIONS[op_name]
    except KeyError:
        raise ValueError(f"Unknown operation: {op_name}") from None
    return operation(a, b)


def apply_twice(func, value):
    return func(func(value))


def compose(f, g):
    def composed(x):
        return f(g(x))

    return composed


print(calculate("add", 2, 3))
print(calculate("mul", 4, 5))
print(apply_twice(lambda s: s + "!", "hey"))
shout = compose(str.upper, lambda s: s + "!")
print(shout("hello"))
print(add.__name__, callable(add), type(add).__name__)
print(sorted(OPERATIONS))
try:
    calculate("pow", 2, 3)
except ValueError as err:
    print("Error:", err)