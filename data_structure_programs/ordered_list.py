"""
Q. Ordered List
    Desc -> Read a List of Numbers from a file and arrange it ascending Order in a List.
        Take user input for a number, if found then pop the number out of the list else insert the
        number in appropriate position.
    I/P -> Read from file the list of Numbers and take user input for a new number
        Logic -> Create a Ordered Linked List having Numbers in ascending order.
    O/P -> The List of Numbers to a File.
"""
from logging_configuration import logging_config

logger = logging_config.get_logger()


def is_found(new_number):
    """
    This function find the number is present or not into the file.
    :param new_number: It's accept a number as a parameter.
    :return: It's return a list of number.
    """
    file = open('numbers.txt', mode='r')
    list_of_numbers = []
    for number in file.read().split(' '):
        list_of_numbers.append(number)
    file.close()
    # initialized found by False
    found = False
    for number in list_of_numbers:
        if number == str(new_number):
            list_of_numbers.remove(str(new_number))
            found = True
    if not found:
        list_of_numbers.append(str(new_number))
    return list_of_numbers


def update_file(list_of_numbers):
    """
    This function update the file.
    :param list_of_numbers: It's accept list of numbers.
    :return: None
    """
    file = open('numbers.txt', mode='w')
    for number in list_of_numbers:
        number = number + ' '
        file.write(number)
    file.close()


if __name__ == '__main__':
    try:
        new_number_ = int(input('Enter a number : '))
        list_of_numbers_ = is_found(new_number_)
        update_file(sorted(list_of_numbers_))
    except ValueError as e:
        print('Enter integer numbers only! Please try again!')
        logger.exception(e)
    except Exception as e:
        print('Oops! Something went wrong! Please try again!')
        logger.exception(e)
