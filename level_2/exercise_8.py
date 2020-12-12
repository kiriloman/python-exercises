# Question:
# Write a program that accepts a comma separated sequence of words as input
# and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def alphabetical_printer(string: str) -> str:
    words = string.split(',')
    words.sort()

    return ','.join(words)


print(alphabetical_printer('without,hello,bag,world'))
