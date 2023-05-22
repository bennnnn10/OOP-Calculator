#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

from Class_Calculator import Calculator
from User_Interface import Interface
from Errors import exceptError

def calculator():
    calcu = Calculator()
    user = Interface()
    error = exceptError()
    
    try:
        #Pseudocode
        #Prompting the user to select an operation and then input it
        math_operation = user.choosing_operations()
        
        #Collect the first number
        #Second number
        #Execute Operations
            #Default Value
        #Result
        #Request if the user wants to make another computation.