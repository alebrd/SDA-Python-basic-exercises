class Car:
    def __init__(self, model, type, engine, color):  # INITIALIZING CAR CLASS BY DEFINING BY ITSELF
        self.model = model  # CREATING PROPRIETIES
        self.type = type  # THE TYPE WILL BE THE TYPE INSERT FROM THE USER AS PARAMETER
        self.engine = engine  # SAME FOR ENGINE ETC ETC
        self.color = color

    def paint(self, new_color):  # defining a function inside the class Car
        print("you're painting the car: ")  # this function will be needed in case I want to change the color of the car
        self.color = new_color  # recalling as in the def init the self.color and attach it to the new_color

    # CREATING VARIABLES BELOW BENZ AND TOYOTA WITH THE 'CLASS CAR'


benz = Car('Amg', 'suv', '2L', 'black')   # AS VISIBLE BENZ IS EQUAL TO CAR(MODEL, TYPE, ENGINE, COLOR)
toyota = Car('Yaris', 'utility', '1000c', 'grey')  # AS VISIBLE TOYOTA IS EQUAL TO CAR(MODEL, TYPE, ENGINE, COLOR)

print(benz.color)  # PRINTING JUST THE BENZ VARIABLE COLOR BY CALLING THE .COLOR METHOD
benz.paint('white')   # CALLING THE PAINT METHOD TO CHANGE THE COLOR OF THE CAR
print(toyota.color)   # PRINTING THE COLOR
print(benz.color)
