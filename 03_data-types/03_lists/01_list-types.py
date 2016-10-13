#!/usr/bin/python3

#Arrays in C, Java, C++ are homogeneous elements

list = ['abcd', 786 , 2.23, 'Venu', 70.2, 3+1.4j]

print (list)          # Prints complete list


tinylist = [123, 'Venu']
# accessed using the slice operator ([ ] and [:])

print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd
print (list[2:])      # Prints elements starting from 3rd element


# plus (+) sign is the list concatenation operator,
# and the asterisk (*) is the repetition operator
#
print (tinylist * 5)  # Prints list two times
newlist = list + tinylist
print (newlist) # Prints concatenated lists


