"""Lab 01 — The interpreter, numbers, strings and lists.

Lab manual: docs/labs/lab01-python-basics.md
Tests:      tests/test_lab01.py

    pytest tests/test_lab01.py -v
"""

# -- numbers ----------------------------------------------------------------


def seconds_to_hms(seconds):
    hours = seconds // 3600
    miuntes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours}:{miuntes:02d}:{secs:02d}"


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 1)


def split_evenly(total, people):
    each = total // people
    remainder = total % people
    return each, remainder


# -- strings ----------------------------------------------------------------


def initials(full_name):
    names = full_name.split()
    result = ""
    i = 0
    while i < len(names):
        result += names[i][0].upper() + "."
        i += 1
    return result


def is_palindrome_word(word):
    cleand = word.strip().lower()
    return cleand == cleand[::-1]


def mask_email(email):
    at_index = email.index("@")
    name = email[:at_index]
    domain = email[at_index:]

    if len(name) <= 2:
        return email
    else:
        masked_name = name[0] + "*" * (len(name) - 2) + name[-1]

    return masked_name + domain


# -- lists ------------------------------------------------------------------


def middle(values):
    n = len(values)
    start = (n - 1) // 2
    end = n // 2 + 1
    return values[start:end]


def rotate_left(values, K):
    if not values:
        return []
    k = K % len(values)
    return values[k:] + values[:k]


def fib_list(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    result = [0, 1]
    a, b = 0, 1
    while len(result) < n:
        a, b = b, a + b
        result.append(b)
    return result


def collatz_steps(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps
