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


def test_addition():
    object1 = Basic_calculator()
    object1.first_number = 5
    object1.operand = '+'
    object1.second_number = 5
    assert object1.show_result()

def test_subtraction():
    object1 = Basic_calculator()
    object1.first_number = 7
    object1.operand = '-'
    object1.second_number = 5
    assert object1.show_result()

