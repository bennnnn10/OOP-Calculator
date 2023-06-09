#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

from Class_Calculator import Calculator
from User_Interface import Interface
from Errors import exceptError
from Header_Design import Design
from BenInterface import BenUserInterface
from NewCalculatorFunction import NewFunction

def calculator():
    calcu = Calculator()
    user = Interface()
    error = exceptError()
    ben = BenUserInterface()
    new = NewFunction()
    
    try:
        #Pseudocode
        #Codeperman
        ben.greetings()

        #Prompting the user to select an operation and then input it
        math_operation = ben.choosing_operations()

        #Collect the first number
        first_number = ben.choosing_first_number()

        #Second number
        second_number = ben.choosing_second_number()
        
        #Execute Operations
        result = None    #Default Value
        if math_operation == 1:
            result = new.addition(first_number, second_number)
        elif math_operation == 2:
            result = new.subtraction(first_number, second_number)
        elif math_operation == 3:
            result = new.multiplication(first_number, second_number)
        elif math_operation == 4:
            result = new.division(first_number, second_number)
        elif math_operation == 5:
            result = new.modulo(first_number, second_number)
        else:
            error.invalid_error()
            calculator()

        #Result
        ben.calculate_result(result)

        #Request if the user wants to make another computation.
        again = ben.do_it_again()
        if again:
            calculator()

    except ZeroDivisionError:
        error.zero_error()
        calculator()

    except ValueError:
        error.value_error()
        calculator()

calculator()