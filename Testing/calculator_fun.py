class Basic_calculator:
    def __init__(self, first_number, operand, second_number):
        self.first_number = first_number
        self.operand = operand
        self.second_number = second_number

    def show_result(self):
        result = []
        if self.operand == '+':
            result = [self.first_number + self.second_number]
        elif self.operand == '-':
            result = [self.first_number - self.second_number]
        return result[0]


object = Basic_calculator(5, '+', 7)

object.first_number = 5
object.operand = '+'
object.second_number = 5

print(object.show_result())


