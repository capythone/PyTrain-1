##### Objects, such as strings or integers of lists are True because they exist.
##### Empty strings, lists, dictionaries etc on the other hand are False because in a way they do not exist.
##### We can use this principle to, for example, only execute a piece of code if a certain list contains any values

numbers = [1, 2, 3, 4]
if numbers:
    print("I found some numbers!")
else:
    print("%s is empty" % (numbers))

numbers = []
if numbers:
    print("I found some numbers!")
else:
    print("%s is empty" % type(numbers))


str = ''
if str:
    print("I found some chars!")
else:
    print("%s is empty" % type(str))

str = ' '
if str:
    print("I found some chars!")
else:
    print("%s is empty" % type(str))


str = 'el '
if str:
    print("I found some chars!")
else:
    print("%s is empty" % type(str))
