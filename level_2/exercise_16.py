# Question:
# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

def get_odd_numbers_1(numbers: list) -> list:
    result = []

    for number in numbers:
        if number % 2 == 1:
            result.append(number)

    return result


def get_odd_numbers_2(numbers: list) -> list:
    return [num for num in numbers if num % 2 == 1]


print(get_odd_numbers_1([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_odd_numbers_2([1, 2, 3, 4, 5, 6, 7, 8, 9]))
