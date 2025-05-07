from colorama import Style, Fore
import os
from sys import platform


def clearCLI():
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def error(txt):
    print(f"{Fore.RED}{Style.BRIGHT}ERROR: {txt}")


def info(txt):
    print(
        f"{Fore.CYAN}{Style.BRIGHT}INFO: {Style.RESET_ALL}{Fore.CYAN}{txt}{Fore.RESET}"
    )


def printColored(txt, color):
    print(f"{color}{txt}{Fore.RESET}")
