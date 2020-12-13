# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers
# as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

# This question is silly because the only 4 digit binary number divisible by 5
# is 1010. Therefore, let's assume that the binary number can have more digits.

def binary_divisible_by_five() -> str:
    binary_numbers = input().split(',')
    result = []

    for binary_number in binary_numbers:
        num = int(binary_number, 2)
        if num % 5 == 0:
            result.append(binary_number)

    return ','.join(result)


print(binary_divisible_by_five())
