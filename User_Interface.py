from termcolor import colored
import pyfiglet

class Interface:

    def choosing_operations(self):
        print("✹" * 78)
        print("\n")
        print(colored("Please choose an operation\n".center(75), "yellow"))
        print(colored("Addition(1), Subtraction(2), Multiplication(3), Division(4), or Modulo(5)\n".center(75), "yellow"))
        print(colored("Choose one of the four math operations (1-5): ".center(75), "cyan"))
        math_operation = int(input("".center(37)))
        print("\n")
        return math_operation

    def choosing_first_number(self):
        first_number = float(input("\033[;1;3mEnter the first number: \033[0m"))
        return first_number
    
    def choosing_second_number(self):
        second_number = float(input("\033[;1;3mEnter the second number: \033[0m"))
        return second_number
    
    def do_it_again(self):
        print("✹" * 78)
        print("\n")
        try_again = input(colored("Would you like to make another calculation? (y/n): ", "yellow"))
        print("\n")
        print("✹" * 78)
        if try_again.lower()  == "y":
            return True
        else:
            print("\n")
            print(pyfiglet.figlet_format("Thank you!".center(11), justify="center"))
            exit()

    def calculate_result(self, result):
        print()
        print("\033[;1;92;3m➺   The result is", result, "\033[0m")