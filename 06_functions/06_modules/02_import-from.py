# import only pi from math module

# from math import pi
import  math
# print("The value of pi is", pi)


# # import all names form
# # the standard module math
#
from math import *
print("The value of pi is", pi)


content = dir(math)

print(content)

# The dir() built-in function
# We can use the dir() function to find out names that are defined inside a module.
#
# For example, we have defined a function add() in the module example that we had in the beginning.