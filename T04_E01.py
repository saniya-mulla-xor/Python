import sys


def divide_line(line):
    try:
        a_text, b_text = line.split()
        a = float(a_text)
        b = float(b_text)
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ValueError:
        return "Invalid input: expected two numbers"
    else:
        return f"{a:g} / {b:g} = {result:g}"


for line in sys.stdin:
    if line.strip():
        print(divide_line(line))