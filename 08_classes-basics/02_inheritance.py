class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduceyourself(self):
        print("My name is " + self.name)
        print("My age is " + str(self.age))


class Teacher(Person):  # this class inherits the class above!
    def __init__(self, name, age):
        self.courses = []  # initialise a new variable
        super().__init__(name, age)  # call the init of Person

    def stateprofession(self):
        print("I am a teacher!")

    def introduceyourself(self):
        super().introduceyourself()  # call the introduceyourself() of the Person
        self.stateprofession()
        print("I teach " + str(self.nrofcourses()) + " course(s)")
        for course in self.courses:
            print("I teach " + course)

    def addcourse(self, course):
        self.courses.append(course)

    def nrofcourses(self):
        return len(self.courses)


author = Teacher("Chandra Babu Naidu", 60)
author.addcourse("Python")
author.addcourse("Golang")
author.introduceyourself()