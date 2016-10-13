#!/usr/bin/python3

# A string in Python must be enclosed with quotes (either single or double quotes)

string = 'Welcome to Python World'

#String manipulation

print (string)          # Prints complete string
print (string[0])       # Prints first character of the string
print (string[2:5])     # Prints characters starting from 3rd to 5th
print (string[2:])      # Prints string starting from 3rd character
print (string * 2)      # Prints string two times
print (string + ", This is Anaconda") # Prints concatenated string


# The plus (+) sign is the string concatenation operator and
# the asterisk (*) is the repetition operator.


# slice operator ([ ] and [:] ) is used to get the  subsets of strings with
# indexes starting at 0 in the beginning of the string.
# and  -1 from the end of the string.
print (string[-4:])      # Prints last 4 charactors of the string
print (string[:])      # Prints last 4 charactors of the string
print (len(string))      # Prints last 4 charactors of the string
# print (string[-23:])     # Prints string in reverse order


# TODO: Exercise#1
#      write some code that defines a variable, name, and assign
#     to it a string that is your name. If your first name is shorter than 5 characters, use your last name.
#     If your last name is also shorter than 5 characters, use the combination of you first and last name.

#
# TODO: Exercise#2
# Can you define a variable middle_letters and assign to it all letters of your name except for
# the first two and the last two?


# TODO: Exercise  #3
# Given the following two words, can you write code that prints out the word humanities
# using only slicing and concatenation? (So, no quotes are allowed in your code.)
# word1 = "human"
# word2 = "opportunities"


# What we have learnt
#
# variable
# value
# assignment to variables
# difference between variables and values
# strings
# integers
# varying variables
# concatenation (e.g. addition of strings)
# indexing
# slicing
# len()