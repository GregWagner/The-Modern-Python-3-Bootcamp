from pyfiglet import figlet_format
from termcolor import colored

def print_art(msg, color="green"):
    colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
    if color not in colors:
          color = "green"

    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)

msg = input("What would you like to print? ")
color = input("What color? ")
print_art(msg, color)
