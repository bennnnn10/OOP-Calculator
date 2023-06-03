from termcolor import colored

from User_Interface import Interface

class BenUserInterface(Interface):
    
    def greetings(self):
        print("\n")
        print(colored("Welcome aboard! Codeperman at your service.".center(75), "cyan"))
        print("\n")
        return
    
    def choosing_first_number(self):
        return super().choosing_first_number()
    
    def choosing_second_number(self):
        return super().choosing_second_number()

    def calculate_result(self, result):
        print("\n")
        print(colored("Initializing completed...", "cyan"))
        print("\n")
        print("\033[;1;92;3mThe total computed is", result, "\033[0m")
        print("\n")