# Scope of a variable is the portion of a program where the variable is recognized.
# Parameters and variables defined inside a function is not visible from outside.
# Hence, they have a local scope.

# Lifetime of a variable is the period throughout which the variable exits in the memory.
# The lifetime of variables inside a function is as long as the function executes.

def my_func():

	print("Value inside function:",x)
	print("Value inside function:",x)
	x = 10
	print("Value inside function:",x+1)
	print("Value inside function:",x)
	print("Value inside function:",x)
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)


# Variables outside of the function are visible from inside. They have a global scope.
# We can read these values from inside the function but cannot change (write) them.
# In order to modify the value of variables outside the function, they must be declared
# as global variables using the keyword global


globvar = 0

def set_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    globvar = 1

def print_globvar():
    print(globvar)     # No need for global declaration to read value of globvar

set_globvar_to_one()
print_globvar()       # Prints 1

##### another example
myGlobal = 5

def func1():
    # global myGlobal
    myGlobal = 42

def func2():
    print(myGlobal)

func1()
func2()