"""
Q. Power of 2
    a. Desc -> This program takes a command-line argument N and prints
       a table of the powers of 2 that are less than or equal to 2^N.
    b. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int.
    c. Logic -> repeat until i equals N.
"""
from sys import argv
from logging_configuration import logging_config

logger = logging_config.get_logger()


def power_of(number_):
    """
    power_of(number_): This function calculate the power of 2 of a number. It's adds all the values
    in a list. It returns a list of power of 2.
    """
    power_value = 0
    list_of_power_of_2 = []
    while power_value != number_:
        list_of_power_of_2.append(2 ** power_value)
        power_value += 1
    return list_of_power_of_2


if __name__ == '__main__':
    try:
        number = int(argv[1])
        # validating the given condition
        if 0 <= number < 31:
            powers_of_2 = power_of(number)
            for values in powers_of_2:
                print(values, ' ', end='')
        else:
            print('Please enter a integer number within (0 <= number < 31) this range!')
    except ValueError:
        print('Enter integer numbers only! Please try again...')
    except IndexError:
        print('Enter value as command line arguments only! Please try again...')
    except Exception as e:
        print('Oops! Something went wrong! Please try again...')
        logger.exception(e)
