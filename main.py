import atexit
import json

try:
    from colorama import Style, Fore
except ImportError:
    print('\n\n"colorama" is nedded for the operation of this code!')
    print('Please install it by running: "pip install colorama"\n\n')
    exit()

from utils import error, info, printColored, clearCLI

# Resets text color and style when the code exits
atexit.register(lambda: print(Style.RESET_ALL))


def loadJSONs():
    success = True
    followers, followings, whitelist = None, None, None

    # Open followers and following jsons.
    try:
        with open("./followers_1.json") as file:
            data = json.load(file)
        followers = list(
            (follower["string_list_data"][0]["value"] for follower in data)
        )
    except FileNotFoundError:
        error(
            'You need to have "followers_1.json" on the same folder as the executable. For more, read the README.'
        )
        success = False
    except json.JSONDecodeError:
        error('The file "followers_1.json" is not formatted correctly.')
        success = False

    try:
        with open("./following.json") as file:
            followings = list(
                following["string_list_data"][0]["value"]
                for following in json.load(file)["relationships_following"]
            )
    except FileNotFoundError:
        error(
            'You need to have "following.json" on the same folder as the executable. For more, read the README.'
        )
        success = False
    except json.JSONDecodeError:
        error('The file "following.json" is not formatted correctly.')
        success = False

    # Open or create the whitelist json
    try:
        with open("./whitelist.json") as file:
            data = json.load(file)
            if data is list:
                error(
                    'The file "whitelist.json" is not formatted correctly. It should be a list.'
                )
                success = False
            else:
                whitelist = list(tag for tag in data)
    except FileNotFoundError:
        with open("./whitelist.json", "w") as file:
            file.write('[\n\t"INSERT_HERE_THE_ACCOUNTS_YOU_DON\'T_WANNA_CHECK_ON"\n]')
        info(
            'whitelist.json has been created. Write in "whitelist.json" the accounts you don\'t wanna check on.\n'
        )
        with open("./whitelist.json") as file:
            whitelist = list(tag for tag in json.load(file))
    except json.JSONDecodeError as e:
        print(e)
        error('The file "whitelist.json" is not formatted correctly.')
        success = False

    return followers, followings, whitelist, success


def compareLists():
    followers, followings, whitelist, success = loadJSONs()

    if not success:
        return

    # Compare lists
    nUnfollorers = 0
    for following in followings:
        if following not in followers and following.lower() not in tuple(
            user.lower() for user in whitelist
        ):
            nUnfollorers += 1
            print(
                f"{(len(str(len(followings)))-len(str(nUnfollorers))) * ' '}{nUnfollorers}. {Fore.RED}{Style.BRIGHT}"
                f"{following.upper()}{Style.RESET_ALL} {(len(max(followings))+2-len(following)) * ' '}"
                "doesn't follow you back."
            )

    if nUnfollorers == 0:
        printColored("Congotulations! Everybody follows you back.", Fore.GREEN)


def printWhitelist():
    whitelist, success = loadJSONs()[2:]

    if not success:
        return

    if "INSERT_HERE_THE_ACCOUNTS_YOU_DON'T_WANNA_CHECK_ON" in whitelist:
        whitelist.remove("INSERT_HERE_THE_ACCOUNTS_YOU_DON'T_WANNA_CHECK_ON")

    if len(whitelist) == 0:
        info("The whitelist is empty")
    else:
        for i in whitelist:
            print(f" - {Fore.GREEN}{Style.BRIGHT}{i}{Style.RESET_ALL}")


def about():
    printColored(
        "Code written by Smartsv (SmartsvXD on Github)\n\nItaly, 2024", Fore.GREEN
    )


def main():
    actions = {
        "Find unfollowers": compareLists,
        "Print whitelist": printWhitelist,
        "About": about,
        f"{Fore.RED}Exit{Fore.RESET}": exit,
    }

    prevInputInvalid = 0
    while 1:
        clearCLI()
        
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Welcome to InstaUnfollowerFinder by Smartsv!{Style.RESET_ALL}\n")

        # Print all the actions
        for n, i in enumerate(actions.keys()):
            print(f" {n+1}. {Style.BRIGHT}{i}{Style.RESET_ALL}")
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


main()
