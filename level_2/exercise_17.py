# Question:
# Write a program that computes the net amount of a bank account based a transaction
# log from console input. The transaction log format is shown as following:
# D 100
# W 200

def net_amount() -> int:
    amount = 0

    while True:
        transaction = input()
        if not transaction:
            return amount

        if transaction.startswith('D'):
            amount += int(transaction.split(' ')[-1])
        elif transaction.startswith('W'):
            amount -= int(transaction.split(' ')[-1])


print(net_amount())
