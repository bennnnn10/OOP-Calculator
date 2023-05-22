class Interface:

    def choosing_operations(self):
        print("Please choose an operation\n")
        print("Addition(1), Subtraction(2), Multiplication(3), or Division(4)")
        print("Choose one of the four math operations (1-4): ")
        math_operation = int(input(""))
        return math_operation

    def choosing_first_number(self):
        first_number = float(input("Enter the first number: "))
        return first_number
    
    def choosing_second_number(self):
        second_number = float(input("Enter the second number: "))
        return second_number