"""
    Basic Calculator Program
"""


def addition(number1, number2):
    """
    This function add two numbers.
    :param number1: It's accept number1 as a parameter.
    :param number2: It's accept number2 as another parameter.
    :return: It's return the addition of two numbers.
    """
    return number1 + number2


def subtraction(number1, number2):
    """
    This function subtract two numbers.
    :param number1: It's accept number1 as a parameter.
    :param number2: It's accept number2 as another parameter.
    :return: It's return the subtraction of two numbers.
    """
    return number1 - number2


def multiplication(number1, number2):
    """
    This function multiply two numbers.
    :param number1: It's accept number1 as a parameter.
    :param number2: It's accept number2 as another parameter.
    :return: It's return the multiplication of two numbers.
    """
    return number1 * number2


def division(number1, number2):
    """
    This function divide two numbers.
    :param number1: It's accept number1 as a parameter.
    :param number2: It's accept number2 as another parameter.
    :return: It's return the division of two numbers.
    """
    if number2 == 0:
        raise ZeroDivisionError('can not divided by zero.')
    else:
        return number1 / number2
