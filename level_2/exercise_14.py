# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

def print_num_of_upper_and_lower_chars(sentence: str):
    upper_chars = 0
    lower_chars = 0

    for char in sentence:
        if char.isupper():
            upper_chars += 1
        elif char.islower():
            lower_chars += 1

    print(f'UPPER CASE {upper_chars}')
    print(f'LOWER CASE {lower_chars}')


print_num_of_upper_and_lower_chars('Hello world!')
