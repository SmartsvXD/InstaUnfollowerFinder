import json, os, atexit

try:
    from colorama import Style, Fore
    print("A")
except:
    print('\n\n"colorama" is nedded for the operation of this code!')
    print("Please install it by running: \"pip install colorama\"\n\n")
    exit()

atexit.register(lambda: print(Style.RESET_ALL))

os.system("clear")

#Open followers and following jsons.
try:
    with open("./followers_1.json") as file:
        followers = json.load(file)
except FileNotFoundError:
    print(f"{Fore.RED}{Style.BRIGHT}You need to have \"followers_1.json\" on the same folder as the executable. For more, read the README.")
    exit()
except json.JSONDecodeError:
    print(f"{Fore.RED}{Style.BRIGHT}The file \"followers_1.json\" is not formatted correctly.")
    exit()

try:
    with open("./following.json") as file:
        followings = json.load(file)
except FileNotFoundError:
    print(f"{Fore.RED}{Style.BRIGHT}You need to have \"following.json\" on the same folder as the executable. For more, read the README.")
    exit()
except json.JSONDecodeError:
    print(f"{Fore.RED}{Style.BRIGHT}The file \"following.json\" is not formatted correctly.")
    exit()

#Open or create the whitelist json
try:
    with open("./whitelist.json") as file:
        whitelist = list(tag.lower() for tag in json.load(file))
except FileNotFoundError:
    with open("./whitelist.json", "w") as file:
        file.write("[\n\t\"INSERT_HERE_THE_ACCOUNTS_YOU_DON'T_WANNA_CHECK_ON\"\n]")        
    print(f"\n{Fore.YELLOW}The whitelist file has been created. Write in \"whitelist.json\" the accounts you don't wanna check on.{Fore.RESET}")
except json.JSONDecodeError:
    print(f"{Fore.RED}{Style.BRIGHT}The file \"whitelist.json\" is not formatted correctly.")
    exit()

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
    print(f"{Fore.GREEN}\nCongotulations! Everybody follows you back.\n")