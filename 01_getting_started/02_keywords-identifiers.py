# There are 33 keywords in Python 3.3. This number can vary slightly in course of time.

# Keywords in Python programming language
# False	class	finally	is	return
# None	continue	for	lambda	try
# True	def	from	nonlocal	while
# and	del	global	not	with
# as	elif	if	or	yield
# assert	else	import	pass
# break	except	in	raise

# All the keywords except True, False and None are in lowercase

#
# Python Identifiers
# Identifier is the name given to entities like class, functions, variables etc. in Python.
#  It helps differentiating one entity from another.
#
# Rules for writing identifiers
# Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_). Names like myClass, var_1 and print_this_to_screen, all are valid example.
# An identifier cannot start with a digit. 1variable is invalid, but variable1 is perfectly fine.
# Keywords cannot be used as identifiers.
#
# >>> global = 1
#   File "<interactive input>", line 1
#     global = 1
#            ^
# SyntaxError: invalid syntax
# We cannot use special symbols like !, @, #, $, % etc. in our identifier.
#
# >>> a@ = 0
#   File "<interactive input>", line 1
#     a@ = 0
#      ^
# SyntaxError: invalid syntax
# Identifier can be of any length.