sentence = "Python's name is derived from the television series Monty Python's Flying Circus."

first_char = sentence[0]
print(first_char)

words = sentence.split()
print(words)
#
print (words[0])       # Prints first element of the list
print (words[1:3])     # Prints elements starting from 2nd till 3rd
print (words[2:])      # Prints elements starting from 3rd element

words.pop()
print(words)
