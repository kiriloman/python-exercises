# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class StringManipulator:

    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input()

    def print_string(self):
        print(self.string.upper())


string_manipulator = StringManipulator()
string_manipulator.get_string()
string_manipulator.print_string()
