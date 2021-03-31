"""
    Test Cases For Basic Calculator Program
"""
import pytest

from pytest_demo import basic_calculator


def test_addition():
    assert basic_calculator.addition(5, 7) == 12
    assert basic_calculator.addition(20, 30) == 50


def test_subtraction():
    assert basic_calculator.subtraction(14, 7) == 7
    assert basic_calculator.subtraction(50, 30) == 20


def test_multiplication():
    assert basic_calculator.multiplication(5, 5) == 25
    assert basic_calculator.multiplication(10, 7) == 70


def test_division():
    assert basic_calculator.division(25, 5) == 5
    with pytest.raises(ZeroDivisionError, match='can not divided by zero.'):
        basic_calculator.division(7, 0)
