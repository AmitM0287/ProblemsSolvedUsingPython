def addition(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):
    if number2 == 0:
        raise ValueError("can't divided by zero!")
    else:
        return number1 / number2


if __name__ == '__main__':
    try:
        division(9, 0)
    except ValueError as e:
        print(e)
