# Program to show
# the control flow when using else block
# in a for loop

# a list of digit
list_of_digits = [0,1,2,3,4,5,6]

# Try changing the input digit for varied results
input_digit = 3

# To take input from user, uncomment the code below
# input_digit = int(input("Enter a digit: "))

# search the input digit in our list
for i in list_of_digits:
	if input_digit == i:
		print("Digit is in the list")
		break
	else:
		print("Digit not found in list")

somestr = "how are you"


import random
# random.shuffle(somestr)
for index, char in enumerate(somestr):
	print("%c exist at index %d" % (char,index))

##### then how ???????

l = list(somestr)  #data conversion .. str -> list -> shuffle -> con
random.shuffle(l)
result = ''.join(l)

for index, char in enumerate(result):
	print("%c exist at index %d" % (char,index))
