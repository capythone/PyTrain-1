# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6,5,3,8,4,2,5,4,11]

# variable to store the sum
sumof = 0

# iterate over the list
for val in numbers:
    sumof += val

# print the sum Output: The sum is 48
print("The sum is", sumof)


### list
colors = ["yellow", "red", "green", "blue", "purple"]
for whatever in colors:
    print("This is color " + whatever)


### touple
colors = "yellow", "red", "green", "blue", "purple"
for whatever in colors:
    print("This is color " + whatever)

##### Since dictionaries are iterable objects as well iterate over the keys of a dictionary
good_reads = {}  # Book is key  rating is val 8
good_reads["Pride and Prejudice"] = 8
good_reads["A Clockwork Orange"] = 9

### iterate over keys only
for book in good_reads:
    print(book)

# print values
for book in good_reads:
    print(book, "has score", good_reads[book])

### get key, value at once
for x, y in good_reads.items():
    print(x + " has score " + str(y)) #String conversion

####### TODO: EXercises
# The function len() returns the length of an iterable item:
#
# len("banana")
# We can use this function to print the length of each word in the color list.
#
# colors = ["yellow", "red", "green", "blue", "purple"]

# Now write a small program that iterates through the list colors and appends all
#           colors that contain the letter r to the list colors_with_r. (Tip: use colors_with_r.append)
#
# colors = ["yellow", "red", "green", "blue", "purple"]
# colors_with_r = []
