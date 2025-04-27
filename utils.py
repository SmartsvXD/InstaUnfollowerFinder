import json
from cliUtils import error, info


def loadJSONs(
    followersPath="./followers_1.josn",
    followingPath="./following.json",
    errorF=error,
):
    success = True
    followers, followings = [], []

    # Open followers and following jsons.
    try:
        with open(followersPath) as file:
            data = json.load(file)
        followers = list(
            (follower["string_list_data"][0]["value"] for follower in data)
        )
    except FileNotFoundError:
        errorF('Error finding "followers_1.json". For more, read the README.')
        success = False
    except json.JSONDecodeError:
        errorF('The file "followers_1.json" is not formatted correctly.')
        success = False

    try:
        with open(followingPath) as file:
            followings = list(
                following["string_list_data"][0]["value"]
                for following in json.load(file)["relationships_following"]
            )
    except FileNotFoundError:
        errorF('Error finding "following.json". For more, read the README.')
        success = False
    except json.JSONDecodeError:
        errorF('The file "following.json" is not formatted correctly.')
        success = False

    return followers, followings, success


def compareLists(
    followersPath="./followers_1.josn",
    followingPath="./following.json",
    infoF=info,
    errorF=error,
):
    followers, followings, success = loadJSONs(
        followersPath=followersPath,
        followingPath=followingPath,
        errorF=errorF,
    )
    whitelist = loadWhitelist(infoF=infoF, errorF=errorF)

    if not success:
        return []

    # Compare lists
    unfollowers = []
    for following in followings:
        if following not in followers and following.lower() not in tuple(
            user.lower() for user in whitelist
        ):
            unfollowers.append(following)

    return unfollowers


def loadWhitelist(infoF=info, errorF=error):
    whitelist = []

    # Open or create the whitelist json
    try:
        # Try to open "whitelist.json"
        with open("./whitelist.json") as file:
            data = json.load(file)
            if data is list:
                errorF('The file "whitelist.json" is not formatted correctly.')
                return []
            else:
                whitelist = list(tag for tag in data)
    except FileNotFoundError:
        # If "whitelist.json" is not found creates it
        with open("./whitelist.json", "w") as file:
            file.write('[\n\t"INSERT_HERE_THE_ACCOUNTS_YOU_DON\'T_WANNA_CHECK_ON"\n]')
        infoF(
            "whitelist.json has been created. Add in the whitelist the accounts you don't wanna check on.\n"
        )
        with open("./whitelist.json") as file:
            whitelist = list(tag for tag in json.load(file))
    except json.JSONDecodeError as e:
        # If "whitelist.json" is not formatted correctly return an error
        print(e)
        errorF('The file "whitelist.json" is not formatted correctly.')
        return []

    if "INSERT_HERE_THE_ACCOUNTS_YOU_DON'T_WANNA_CHECK_ON" in whitelist:
        whitelist.remove("INSERT_HERE_THE_ACCOUNTS_YOU_DON'T_WANNA_CHECK_ON")

    return whitelist


def saveWhitelist(whitelist):
    with open("./whitelist.json", "w") as f:
        json.dump(tuple(set(whitelist)), f)


def addToWhiteList(name, infoF=info, errorF=error):
    whitelist = loadWhitelist(infoF=infoF, errorF=errorF)

    whitelist.append(name)
    
    saveWhitelist(whitelist)
    
def removeFromWhiteList(name, infoF=info, errorF=error):
    whitelist = loadWhitelist(infoF=infoF, errorF=errorF)

    whitelist.remove(name)
    
    saveWhitelist(whitelist)
