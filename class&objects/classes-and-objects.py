class Animal:
    name = ""  # class variable
    age = 0  # class variable

    def __init__(self, name='Jenna', age=2):  # s pecial method used for instantiation - that is object creation
        self.name = name  # setting default name when creating the object
        self.age = age  # setting default age when creating the object

    def print_details(self):  # class method printing state of the instance
        print(f"Name: {self.name}, age: {self.age}")


animal1 = Animal('bob', 5)



