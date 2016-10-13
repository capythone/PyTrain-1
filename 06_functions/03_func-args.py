# def greet(name):
# 	"""This function greets to
# 	the person passed in as
# 	parameter"""
# 	print("Hello, " + name + ". Good morning!")
# 	print("Hello, " + name + ". Good night!")
#
# greet('venu')
# greet('venu', 'james bond')



def greet(name, msg = "Good morning!"):
   """
   This function greets to the person with the provided message.

   If message is not provided, it defaults to "Good morning!"
   """

   print("Hello",name + ', ' + msg)

greet("Kate")
greet("Bruce","How do you do?")