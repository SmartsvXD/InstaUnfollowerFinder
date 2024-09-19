from colorama import Style, Fore

def error(txt):
    print(f"{Fore.RED}{Style.BRIGHT}ERROR: {txt}")
    exit()

def info(txt):
    print(f'{Fore.CYAN}{Style.BRIGHT}INFO: {Style.RESET_ALL}{Fore.CYAN}{txt}{Fore.RESET}')