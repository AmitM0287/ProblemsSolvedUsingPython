def square_value(range_):
    """
    This function is used to print the square values between the given range.
    :param range_: It's accept the range as a parameter.
    :return: It's return the square value.
    """
    _number = 1
    while _number <= range_:
        square = _number * _number
        yield square
        _number += 1


if __name__ == '__main__':
    values = square_value(10)
    print(values.__next__())
    for numbers in values:
        print(numbers)
