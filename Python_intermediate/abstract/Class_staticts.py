# class Person:
#     some_class_var = 10
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} ma {self.age} lat"
#
#
# class Student(Person):
#     def __init__(self, name, age, scholarship):
#         Person.__init__(self, name, age)
#         self.scholarship = scholarship
#
#     def show_finance(self):
#         return self.scholarship
#
#     @classmethod
#     def do_some_class_variable_dependent_op(cls):
#         cls.some_class_var += 1
#
#     @staticmethod
#     def do_nothing_dependent_utility_op(a, b):
#         return a + b
#
#     @classmethod
#     def create_default(cls):
#         return cls("default", 10, 10)
#
#
# student = Student("basar", 10, 10)
# print(Student.some_class_var)
# Student.do_some_class_variable_dependent_op()
# print(Student.some_class_var)

class Employee:
    # REMEMBER THESE ARE CLASS VARIABLES. NOT INSTANCE VARIABLES
    num_of_emps = 0  # WITH THE CLASS METHOD WE WORK WITH THE CLASS VARIABLES
    raise_amt = 1.04  # WE DON'T WORK WITH THE INSTANCE VARIABLE

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'Employee', 60000)

# Employee.set_raise_amt(1.05)  # is the same thing
# Employee.raise_amt = 1.05  # same thing we changing class variables

# emp2.set_raise_amt(1.05)  # doing it with an instantiated object will still change the class variable
#
# print(Employee.raise_amt)
# print(emp1.raise_amt)
# print(emp2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Jackson-90000'

new_emp1 = Employee.from_string(emp_str_1)
print(new_emp1.email)
print(new_emp1.pay)
