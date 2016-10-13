def greet(name):
	"""This function greets to the person passed in as parameter"""
	print(name)
	print(name+1000)
	print("Hello, " + str(name) + ". Good morning!")

# greet(1000)
# greet(123.4565)
# greet('venu')



#
# # The first string after the function header is called the docstring and
# # is short for documentation string. It is used to explain in brief, what a function does.
#
# # generally use triple quotes so that docstring can extend up to multiple lines.
# # This string is available to us as __doc__ attribute of the function.
#
print(greet.__hash__())
print(hash(greet))
# print(greet.__doc__)
#
# # return statement can contain expression which gets evaluated and the value is returned.
# # If there is no expression in the statement or the return statement itself is not present inside a function,
# # then the function will return the None object
#
# print(greet("May"))
