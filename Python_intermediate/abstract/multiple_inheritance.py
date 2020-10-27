class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_finance(self):
        return 0

    def __str__(self):
        return f"{self.name} ma {self.age} lat"


class Employee(Person):
    def __init__(self, name, age, rate, num_of_hour):
        Person.__init__(self, name, age)
        self.rate = rate
        self.num_of_hour = num_of_hour

    def show_finance(self):
        return self.rate * self.num_of_hour

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Student(Person):
    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship

    def __str__(self):
        return f"{self.name} is {self.age} years old2"


class WorkingStudent(Employee, Student):
    def __init__(self, name, age, rate, num_of_hour, scholarship):
        Employee.__init__(self, name, age, rate, num_of_hour)
        Student.__init__(self, name, age, scholarship)

    def show_finance(self):
        return self.rate * self.num_of_hour + self.scholarship


person = WorkingStudent("basar", 31, 10, 10, 300)
print(person)
print(person.show_finance())
print(WorkingStudent.__mro__)
