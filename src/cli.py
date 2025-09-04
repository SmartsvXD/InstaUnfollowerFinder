import atexit
import webbrowser

try:
    from colorama import Style, Fore
except ImportError:
    print('\n\n"colorama" is nedded for the operation of this code!')
    print('Please install it by running: "pip install colorama"\n\n')
    input("(Press ENTER to exit)")
    exit()

from src.cli_utils import printColored, clearCLI, info
from src.utils import loadJSONs, compareLists, loadWhitelist, checkVersion

# Resets text color and style when the code exits
atexit.register(lambda: print(Style.RESET_ALL))


def printUnfollowers():
    followers, followings, whitelist, success = loadJSONs()
    unfollowers = compareLists()

    if not success:
        return

    # Compare lists
    nUnfollorers = 0
    for unfollower in unfollowers:
        nUnfollorers += 1
        print(
            f"{(len(str(len(followings))) - len(str(nUnfollorers))) * ' '}{nUnfollorers}. {Fore.RED}{Style.BRIGHT}"
            f"{unfollower.upper()}{Style.RESET_ALL} {(len(max(followings)) + 2 - len(unfollower)) * ' '}"
            "doesn't follow you back."
        )

    if nUnfollorers == 0:
        printColored("Congotulations! Everybody follows you back.", Fore.GREEN)


def printWhitelist():
    whitelist = loadWhitelist()

    if len(whitelist) == 0:
        info("The whitelist is empty")
    else:
        for i in whitelist:
            print(f" - {Fore.GREEN}{Style.BRIGHT}{i}{Style.RESET_ALL}")


def about():
    printColored(
        "Code written by SmartsvXD\n\nItaly, 2024-2025", Fore.GREEN
    )


def main():
    actions = {
        "Find unfollowers": printUnfollowers,
        "Open Meta Account Center": lambda: webbrowser.open(
            "https://accountscenter.instagram.com/info_and_permissions/?theme=dark"
        ),
        "Print whitelist": printWhitelist,
        "About": about,
        f"{Fore.RED}Exit{Fore.RESET}": exit,
    }

    prevInputInvalid = 0
    while 1:
        clearCLI()

        newVersion = checkVersion()
        if newVersion[0]:
            print(
                f"{Fore.GREEN}{Style.BRIGHT}A new version is available! {newVersion[1]} -> {newVersion[2]}{Style.RESET_ALL}"
            )
            print(
                f"{Fore.YELLOW}Download it using the link:{Fore.RESET}{Style.BRIGHT} https://github.com/SmartsvXD/InstaUnfollowerFinder/releases/latest {Style.RESET_ALL}\n"
            )

        print(
            f"{Fore.MAGENTA}{Style.BRIGHT}Welcome to InstaUnfollowerFinder by SmartsvXD!{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}{Style.DIM} v{newVersion[1]}{Style.RESET_ALL}\n"
        )

        # Print all the actions
        for n, i in enumerate(actions.keys()):
            print(f" {n + 1}. {Style.BRIGHT}{i}{Style.RESET_ALL}")
        print()

        # Print something if the previrous input was not valid
        if prevInputInvalid:
            printColored("Invalid input!", Fore.RED)
            prevInputInvalid = 0

        # Ask and run user input
        try:
            selection = (
                int(input(f"{Fore.YELLOW}Select what you wanna do: {Fore.RESET}")) - 1
            )
            clearCLI()
            tuple(actions.values())[selection]()
            input(
                f"{Fore.YELLOW}{Style.DIM}\n(Press ENTER to go back to menu){Style.RESET_ALL}"
            )
        except (IndexError, ValueError):
            prevInputInvalid = 1
