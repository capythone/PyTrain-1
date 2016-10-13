# if test expression:
#     statement(s)

# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

######### Nested if

# In this program, we input a number check if the number is positive or
# negative or zero and display
# an appropriate message
# This time we use nested if
#
# num = float(input("Enter a number: "))
# if num >= 0:
#     if num == 0:
#         print("Zero")
#     else:
#         print("Positive number")
# else:
#     print("Negative number")

###### and, or , not
word = "apple"
if "a" in word and "b" in word:
    print("Both a and b are in " + word)
else:
    print('a and b do not exist in word')
