def linear_search(items, target):
    comparisons = 0
    for index, item in enumerate(items):
        comparisons += 1
        if item == target:
            return index, comparisons
    return -1, comparisons


def binary_search(items, target):
    low = 0
    high = len(items) - 1
    comparisons = 0

    while low <= high:
        middle = (low + high) // 2
        comparisons += 1
        if items[middle] == target:
            return middle, comparisons
        if items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1, comparisons


def first_occurrence(items, target):
    low = 0
    high = len(items) - 1
    result = -1

    while low <= high:
        middle = (low + high) // 2
        if items[middle] == target:
            result = middle
            high = middle - 1
        elif items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return result


numbers = list(range(0, 200, 2))
print("linear 150:", linear_search(numbers, 150))
print("binary 150:", binary_search(numbers, 150))
print("linear 151:", linear_search(numbers, 151))
print("binary 151:", binary_search(numbers, 151))
print("first 5 in [1,3,5,5,5,8]:", first_occurrence([1, 3, 5, 5, 5, 8], 5))