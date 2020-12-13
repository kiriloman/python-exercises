# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

def print_num_of_letters_and_digits_1(sentence: str):
    num_of_letters = 0
    num_of_digits = 0

    for char in sentence:
        if ord(char) in range(ord('a'), ord('z') + 1):
            num_of_letters += 1

        try:
            int(char)
            num_of_digits += 1
        except ValueError:
            continue

    print(f'LETTERS {num_of_letters}')
    print(f'DIGITS {num_of_digits}')


def print_num_of_letters_and_digits_2(sentence: str):
    num_of_letters = 0
    num_of_digits = 0

    for char in sentence:
        if char.isalpha():
            num_of_letters += 1
        if char.isnumeric():
            num_of_digits += 1

    print(f'LETTERS {num_of_letters}')
    print(f'DIGITS {num_of_digits}')


import re


def print_num_of_letters_and_digits_3(sentence: str):
    num_of_letters = 0
    num_of_digits = 0

    for char in sentence:
        if re.search('[a-zA-Z]', char):
            num_of_letters += 1
        if re.search('\\d', char):
            num_of_digits += 1

    print(f'LETTERS {num_of_letters}')
    print(f'DIGITS {num_of_digits}')


print_num_of_letters_and_digits_1('hello world! 123')
print_num_of_letters_and_digits_2('hello world! 123')
print_num_of_letters_and_digits_3('hello world! 123')
