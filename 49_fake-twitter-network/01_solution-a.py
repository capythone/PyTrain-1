from collections import defaultdict

def findUserFollowers(user):
    followersList = []
    for line in open("twitter.txt"):
        follower, followee = line.strip().split(';')
        if followee == user:
            followersList.append(follower)
    return followersList


def findWhomUserFollowing(user):
    followeesList = []
    for line in open("twitter.txt"):
        follower, followee = line.strip().split(';')
        if follower == user:
            followeesList.append(followee)
    return followeesList

def usersAdjancyList():
    twitter_graph_dict = defaultdict(list)
    for line in open("twitter.txt"):
        follower, followee = line.strip().split(';')
        twitter_graph_dict[follower].append(followee)
    return twitter_graph_dict


def printFollowerByTouple():
    toupleList = []
    twitter_graph_dict = defaultdict(list)

    for line in open("twitter.txt"):
        follower, followee = line.strip().split(';')
        toupleList.append((follower,followee))

    for k, v in toupleList:
        twitter_graph_dict[k].append(v)

    return twitter_graph_dict

for k, v in printFollowerByTouple().items():
# for k, v in printAllUsersFollowers().items():
    print("friends of ", k, " are# ", v)