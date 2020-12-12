# Question
# Write a program that accepts sequence of lines as input
# and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

def list_to_upper(words: list) -> list:
    return [str(word).upper() for word in words]


upper_words = list_to_upper(['Hello world', 'Practice makes perfect'])
for upper_word in upper_words:
    print(upper_word)
