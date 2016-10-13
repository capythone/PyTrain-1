class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def introduceyourself(self):
    #     print("My name is " + self.name)
    #     print("My age is " + str(self.age))


author = Person("Maarten", 30)
# author.introduceyourself()
print("My name is " + author.name)
print("My age is " + str(author.age))


