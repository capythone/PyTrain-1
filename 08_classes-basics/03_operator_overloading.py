class Tweet:
    def __init__(self, message, time):
        self.message = message
        self.time = time  # we will assume here that time is a numerical value

    def __lt__(self, other):
        return self.time < other.time

    def __gt__(self, other):
        return self.time > other.time

    def __contains__(self, word):
        print("contains operator")


# Implement the method
oldtweet = Tweet("this is an old tweet", 20)
newtweet = Tweet("this is a new tweet", 30)
verynewtweet = Tweet("this is a very new tweet", 40)

print(newtweet > oldtweet)

tweets = [verynewtweet,newtweet,oldtweet]

for tweet in sorted(tweets):
    print(tweet.message)