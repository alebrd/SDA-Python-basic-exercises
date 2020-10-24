import calculator_fun


def test_addition():
    object1 = calculator_fun.Basic_calculator(5, '+', 5)
    object1.first_number = 5
    object1.operand = '+'
    object1.second_number = 5
    assert object1.show_result()


def test_subtraction():
    object1 = calculator_fun.Basic_calculator(7, '-', 5)
    object1.first_number = 7
    object1.operand = '-'
    object1.second_number = 5
    assert object1.show_result()

