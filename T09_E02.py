def sum_of_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


def reverse_string(text):
    if len(text) <= 1:
        return text
    return reverse_string(text[1:]) + text[0]


def is_palindrome(text):
    cleaned = "".join(character.lower() for character in text if character.isalnum())

    def compare_ends(value):
        if len(value) <= 1:
            return True
        if value[0] != value[-1]:
            return False
        return compare_ends(value[1:-1])

    return compare_ends(cleaned)


print(sum_of_digits(12345))
print(sum_of_digits(-907))
print(sum_of_digits(0))
print(reverse_string("recursion"))
print(repr(reverse_string("")))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("Python"))
print(is_palindrome(""))