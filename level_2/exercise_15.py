# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

def compute_important_value(number: int) -> int:
    return number + number*11 + number*111 + number*1111


print(compute_important_value(9))
