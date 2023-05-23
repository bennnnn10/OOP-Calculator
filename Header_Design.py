from termcolor import colored
import pyfiglet

class Design:

    def colored_ascii(text, color):
        ascii_art = pyfiglet.figlet_format(text, font="speed", justify="center")
        colored_ascii_art = colored(ascii_art, color)
        print(colored_ascii_art)

    print("✹" * 78)
    colored_ascii("Calculator", "cyan")
    print(colored("Press <enter> to start!".center(75), "yellow"))
    input("".center(39))