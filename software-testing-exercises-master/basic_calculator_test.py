from basic_calculator import BasicCalculator


def test_addition():
    object = BasicCalculator()
    object.provide_number(10)
    object.provide_operand('+')
    object.provide_number(5)
    assert object.show_result()[0] == 15


def test_subtraction():
    object = BasicCalculator()
    object.provide_number(13)
    object.provide_operand('-')
    object.provide_number(21)
    with pytest.raises(Exception):
        assert object.show_result()