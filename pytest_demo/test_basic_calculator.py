from pytest_demo import basic_calculator


def test_addition():
    assert basic_calculator.addition(7, 8) == 15
    assert basic_calculator.addition(5, 7) == 12


def test_subtraction():
    assert basic_calculator.subtraction(8, 4) == 4
    assert basic_calculator.subtraction(9, 2) == 7


def test_multiplication():
    assert basic_calculator.multiplication(5, 7) == 35
    assert basic_calculator.multiplication(4, 7) == 28


def test_division():
    assert basic_calculator.division(8, 2) == 4
    assert basic_calculator.division(49, 7) == 7
