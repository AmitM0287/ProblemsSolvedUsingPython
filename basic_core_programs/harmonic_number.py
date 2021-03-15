"""
Q. Harmonic Number
    a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
    b. I/P -> The Harmonic Value N. Ensure N != 0
    c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
    d. O/P -> Print the Nth Harmonic Value.
"""
from logging_configuration import logging_config

logger = logging_config.get_logger()


def harmonic_value_of(number_):
    """
    This function calculate the n-th harmonic value.
    :param number_: It's accept a number_ as a parameter.
    :return: It's return n-th harmonic value of that number_.
    """
    harmonic_value_ = 0
    for number_ in range(1, number_+1):
        harmonic_value_ += 1/number_
    return round(harmonic_value_, 4)


if __name__ == '__main__':
    try:
        number = int(input("Enter a number to get it's Harmonic Value : "))
        if number > 0:
            harmonic_value = harmonic_value_of(number)
            print('The Harmonic value of ', number, ' is : ', harmonic_value)
        else:
            print('Enter positive integers only! Please try again...')
    except ValueError as e:
        print('Enter integers only! Please try again...')
        logger.exception(e)
    except Exception as e:
        print('Oops! Something went wrong! Please try again...')
        logger.exception(e)
