#!/usr/bin/python3

import sys
from InstagramAPI import InstagramAPI

def getFollowers(api, user_id):
    followers = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')

    return followers


def getFollowings(api, user_id):
    api.getUsernameInfo(user_id)
    api.LastJson
    following = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''
        _ = api.getUserFollowings(user_id, maxid=next_max_id)
        following.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')

    return following


def printUnfollowers():
    print("Hello, " + sys.argv[1] + "!\n")

    api = InstagramAPI(sys.argv[1], sys.argv[2])
    api.login()

    user_id = api.username_id

    followers = getFollowers(api, user_id)
    followings = getFollowings(api, user_id)

    print("Total followers: " + str(len(followers)))
    print("Total followings: " + str(len(followings)))
    print()

    totalUnfollowers = 0

    for following in followings:
        isUnfollower = True
        for follower in followers:
            if follower["username"] == following["username"]:
                isUnfollower = False
                break
        
        if isUnfollower:
            totalUnfollowers += 1
            print("Unfollower " + str(totalUnfollowers) + ": " + following["username"])


printUnfollowers()