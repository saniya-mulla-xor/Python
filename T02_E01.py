def fizzbuzz(n):
    results = []
    for number in range(1, n + 1):
        if number % 15 == 0:
            results.append("FizzBuzz")
        elif number % 3 == 0:
            results.append("Fizz")
        elif number % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(number))
    return results


n = int(input())
for item in fizzbuzz(n):
    print(item)