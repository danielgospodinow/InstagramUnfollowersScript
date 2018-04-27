#!/usr/bin/python3

from utils.utils import *

username, password = getUserCreditials()
print("Hello, " + username + "!\n")

unfollowers = getUnfollowers(getInstaAPI(username, password))
for i, unfollower in enumerate(unfollowers):
    print ("Unfollower " + str(i + 1) + ": " + unfollower["username"])
