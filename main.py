import json, os, importlib

try:
    from colorama import Style, Fore
except:
    print('"colorama" is nedded for the operation of this code!')
    print("Please install it by running: \"pip install colorama\"")

os.system("clear")

with open("./followers.json") as file:
    followers = json.load(file)

with open("./following.json") as file:
    followings = json.load(file)

with open("./whitelist.json") as file:
    whitelist = list(tag.lower() for tag in json.load(file))

tagFollowers = list(follower["string_list_data"][0]['value'] for follower in followers)
tagFollowings = list(following["string_list_data"][0]['value'] for following in followings['relationships_following'])

i = 0
for tagFollowing in tagFollowings:
    if tagFollowing not in tagFollowers and tagFollowing.lower() not in whitelist:
        i += 1
        print(f"{(len(str(len(tagFollowings)))-len(str(i))) * ' '}{i}. {Fore.RED}{Style.BRIGHT}{tagFollowing.upper()}{Style.RESET_ALL} {(len(max(tagFollowings))+2-len(tagFollowing)) * ' '} doesn't follow you back.")