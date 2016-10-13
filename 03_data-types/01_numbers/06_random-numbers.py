import random

# Output: 16
#
print(random.randrange(10,20))

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Get random choice
print(random.choice(x))

str = 'hello world python we are to become experts in python'
words =  str.split(' ')
print(random.choice(words))

# Shuffle x
random.shuffle(x)

# Print the shuffled x
print(x)

# Print random element
print(random.random())