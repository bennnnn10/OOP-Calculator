from termcolor import colored

class exceptError:

    def invalid_error(self):
        print()
        print(colored("Invalid operation number.\n".center(75), "red"))

    def zero_error(self):
        print()
        print(colored("Error: Cannot divide by zero.\n".center(75), "red"))

    def value_error(self):
        print()
        print(colored("Error: Invalid input.\n".center(75), "red"))