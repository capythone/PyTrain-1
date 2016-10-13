# Print range
# Output: range(0, 200)
print(range(200))

# Print list of range
# from 0 to 10 Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))

# Print list of range between
# 2 to 8 Output: [2, 3, 4, 5, 6, 7]
print(list(range(2,8)))

# Print list of range between
# 2 to 20 with a difference of 3
# Output: [2, 5, 8, 11, 14, 17]
print(list(range(2,20,3)))

# simple
for e in range(1,15,2): #odd numbers
    print(e)

##### Program to iterate through a list using indexing

# List of genre
genre = ['pop','rock','jazz']

# iterate over the list using index
for i in range(len(genre)):
	print("I like",genre[i]) #inconsistent indent

for item in genre:
    print(item)