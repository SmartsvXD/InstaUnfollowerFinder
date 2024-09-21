import atexit

try:
    from colorama import Style, Fore
except:
    print('\n\n"colorama" is nedded for the operation of this code!')
    print("Please install it by running: \"pip install colorama\"\n\n")
    exit()

from utils import *

#Resets text color and style when the code exits
atexit.register(lambda: print(Style.RESET_ALL))

def loadJSONs():
    success = True

    followers, followings, whitelist = None, None, None

    #Open followers and following jsons.
    try:
        with open("./followers_1.json") as file:
            followers = json.load(file)
    except FileNotFoundError:
        error("You need to have \"followers_1.json\" on the same folder as the executable. For more, read the README.")
        success = False
    except json.JSONDecodeError:
        error("The file \"followers_1.json\" is not formatted correctly.")
        success = False

    try:
        with open("./following.json") as file:
            followings = json.load(file)
    except FileNotFoundError:
        error("You need to have \"following.json\" on the same folder as the executable. For more, read the README.")
        success = False
    except json.JSONDecodeError:
        error("The file \"following.json\" is not formatted correctly.")
        success = False

    #Open or create the whitelist json
    try:
        with open("./whitelist.json") as file:
            whitelist = list(tag.lower() for tag in json.load(file))
    except FileNotFoundError:
        with open("./whitelist.json", "w") as file:
            file.write("[\n\t\"INSERT_HERE_THE_ACCOUNTS_YOU_DON'T_WANNA_CHECK_ON\"\n]")        
        info("The whitelist file has been created. Write in \"whitelist.json\" the accounts you don't wanna check on.\n")
        with open("./whitelist.json") as file:
            whitelist = list(tag.lower() for tag in json.load(file))
    except json.JSONDecodeError:
        error("The file \"whitelist.json\" is not formatted correctly.")
        success = False

    return followers, followings, whitelist, success

def compareLists():
    followers, followings, whitelist, success = loadJSONs()

    if not success:
        return

    #Prepare lists to compare
    tagFollowers = list(follower["string_list_data"][0]['value'] for follower in followers)
    tagFollowings = list(following["string_list_data"][0]['value'] for following in followings['relationships_following'])

    #Compare lists
    nUnfollorers = 0
    for tagFollowing in tagFollowings:
        if tagFollowing not in tagFollowers and tagFollowing.lower() not in whitelist:
            nUnfollorers += 1
            print(f"{(len(str(len(tagFollowings)))-len(str(nUnfollorers))) * ' '}{nUnfollorers}. {Fore.RED}{Style.BRIGHT}{tagFollowing.upper()}{Style.RESET_ALL} {(len(max(tagFollowings))+2-len(tagFollowing)) * ' '} doesn't follow you back.")

    if nUnfollorers == 0:
        printColored("Congotulations! Everybody follows you back.", Fore.GREEN)

def about():
    printColored("Code written by Smartsv (SmartsvXD on Github)\n\nItaly, 2024", Fore.GREEN)

actions = {
    "Find unfollowers": compareLists,
    "About": about, 
    f"{Fore.RED}Exit{Fore.RESET}": exit
}

prevInputInvalid = 0
while 1:
    clearCLI()

    for n, i in enumerate(actions.keys()):
        print(f"{n+1}. {Style.BRIGHT}{i}{Style.RESET_ALL}")
    print()

    if prevInputInvalid:
        printColored("Invalid input!", Fore.RED)
        prevInputInvalid = 0

    try:
        selection = int(input(f"{Fore.YELLOW}Select what you wanna do: {Fore.RESET}"))-1
        clearCLI()
        tuple(actions.values())[selection]()
        input(f"{Fore.YELLOW}{Style.DIM}\n(Press ENTER to go back to menu){Style.RESET_ALL}")
    except (IndexError, ValueError):
        prevInputInvalid = 1