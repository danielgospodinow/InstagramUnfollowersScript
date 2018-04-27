import sys
from utils.trie import *
from InstagramAPI import InstagramAPI

def getUserCreditials():
    return sys.argv[1], sys.argv[2]

    
def extractNames(people):
    names = []
    for person in people:
        names.append(person["username"])
    return names


def getInstaAPI(username, password):
    api = InstagramAPI(username, password)
    api.login()

    return api


def getUnfollowerNames(api):
    followings = api.getTotalFollowings(api.username_id)
    followers = api.getTotalFollowers(api.username_id)

    print("Total followers: " + str(len(followers)))
    print("Total followings: " + str(len(followings)) + "\n")

    unfollowers = []
    trieRoot = getRootOfTrie(extractNames(followers))

    for following in extractNames(followings):
        if not hasWord(trieRoot, following):
            unfollowers.append(following)
    
    return unfollowers


def getUnfollowers(api):
    followings = api.getTotalFollowings(api.username_id)
    followers = api.getTotalFollowers(api.username_id)

    print("Total followers: " + str(len(followers)))
    print("Total followings: " + str(len(followings)) + "\n")

    unfollowers = []

    for following in followings:
        isUnfollower = True
        for follower in followers:
            if following["username"] == follower["username"]:
                isUnfollower = False
                break
        
        if isUnfollower:
            unfollowers.append(following)
    
    return unfollowers