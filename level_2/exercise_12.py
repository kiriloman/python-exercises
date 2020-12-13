# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def numbers_with_even_digits_between(start: int, end: int) -> str:
    result = []

    for num in range(start, end + 1):
        if valid_even_digits(num):
            result.append(str(num))

    return ','.join(result)


def valid_even_digits(num: int) -> bool:
    if num // 10 == 0 and num % 2 == 0:
        return True

    while num != 0:
        if num % 2 != 0:
            return False

        num //= 10

    return True


print(numbers_with_even_digits_between(1000, 3000))
