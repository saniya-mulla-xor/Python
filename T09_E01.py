def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def countdown(n):
    if n <= 0:
        return []
    return [n] + countdown(n - 1)


def sum_list(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])


print(factorial(0), factorial(1), factorial(5))
print(factorial(20))
print(countdown(5))
print(countdown(0))
print(sum_list([1, 2, 3, 4]))
print(sum_list([]))
try:
    factorial(-3)
except ValueError as err:
    print("Error:", err)