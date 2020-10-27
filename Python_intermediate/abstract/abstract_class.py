from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def move(self):
#         pass
#
#     @abstractmethod
#     def eat(self):
#         pass
#
#
# class Mammal(Animal):  # STILL ABSTRACT METHODS CAUSEE JUST EAT IS DEFINED
#     def eat(self):
#         return 'Eat'
#
# class Dog(Mammal):  # NO ANYMORE ABSTRACT CAUSE BOTH ABSTRACT METHODS ARE DEFINED
#     def move(self):
#         return 'Run'
#
#
# animal1 = Dog()
#
# print(animal1.eat())
#
# print(animal1.move())
#
# animal2 = Mammal()  # RUN ERRORS CAUSE ITS STILL AN ABSTRACT CLASS
# print(animal2.eat())
# print(animal2.move())

'''Abstract classes and method have sense just when you design an application 
 in OPS way, so basically when you follow the concept of object-oriented
 programming you have to follow some patterns and one 
 '''


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print('is a laptop')


class Whiteboard(Computer):
    def write(self):
        print("it's writing")


class Programmer:
    def work(self, com):
        print('Solving problems')
        com.process()


# com = Computer()
com1 = Laptop()
# com.process()
com2 = Whiteboard()

programmer1 = Programmer()
programmer1.work(com2)

