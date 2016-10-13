# Java use braces { } to define a block of code. Python uses indentation.


# A code block (body of a function, loop etc.) starts with indentation and
# ends with the first unindented line. The amount of indentation is up to you,
#  but it must be consistent throughout that block.

for i in range(1,11):
    print(i)   # for
    if i == 5:
        break
        print("this belongs to if condition headline")
    if i == 6:
        print("something else")
    print("this belong for head line")
#
# import sys
#
# file_name = "/Users/ref823/PythONE/BootCamp/01_getting_started/helloworld.txt"
# try:  #header line
#   # open file stream             #suite
#   file = open(file_name, "w")
# except IOError:
#   print ("There was an error writing to", file_name)
#   sys.exit()
# print ("Enter '", file_finish,)
# print ("' When finished")
# while file_text != file_finish:
#   file_text = raw_input("Enter text: ")
#   if file_text == file_finish:
#     # close the file
#     file.close
#     break
#   file.write(file_text)
#   file.write("\n")
# file.close()
# file_name = input("Enter filename: ")
# if len(file_name) == 0:
#   print ("Next time please enter something")
#   sys.exit()
# try:
#   file = open(file_name, "r")
# except IOError:
#   print ("There was an error reading file")
#   sys.exit()
# file_text = file.read()
# file.close()
# print (file_text)

if True:
    print('Hello')
    a = 5

if True: print('Hello'); a = 5 #both are same

# Multiline comment

''' this is an example of
 multi line comments '''

"""This is also a
perfect example of
multi-line comments"""

# Docstring is short for documentation string.
#
# It is a string that occurs as the first statement in a module, function, class, or method definition. We must write what a function/class does in the docstring.
#
# Triple quotes are used while writing docstrings.

def double(num):
    """Function to
    so and so
    sths
    the ass
    mand
    double the value"""
    return 2*num

#
