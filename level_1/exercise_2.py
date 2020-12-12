# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def factorial(number: int) -> int:
    if number == 0:
        return 1

    result = 1
    for i in range(1, number + 1):
        result *= i

    result


def recursive_factorial(number: int) -> int:
    if number < 0:
        return 0
    if number == 0:
        return 1

    return number * recursive_factorial(number - 1)


factorial(8)
print(str(recursive_factorial(8)))
