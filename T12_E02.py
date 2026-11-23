def bubble_sort(items):
    result = list(items)
    swaps = 0

    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swaps += 1
                swapped = True
        if not swapped:
            break

    return result, swaps


def selection_sort(items):
    result = list(items)
    swaps = 0

    for index in range(len(result) - 1):
        smallest = index
        for current in range(index + 1, len(result)):
            if result[current] < result[smallest]:
                smallest = current
        if smallest != index:
            result[index], result[smallest] = result[smallest], result[index]
            swaps += 1

    return result, swaps


data = [64, 25, 12, 22, 11]
print("input:    ", data)
print("bubble:   ", bubble_sort(data))
print("selection:", selection_sort(data))
print("already sorted bubble:", bubble_sort([1, 2, 3, 4]))
print("input unchanged:", data)