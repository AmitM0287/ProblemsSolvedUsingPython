"""
Bubble Sort
Desc -> Reads in integers prints them in sorted order using Bubble Sort
I/P -> read in the list ints
O/P -> Print the Sorted List
"""
from numpy import zeros
from logging_configuration import logging_config

logger = logging_config.get_logger()


def bubble_sort(array_, len_array):
    """
    This function sorted the array in ascending order.
    :param array_: It's accept array as a parameter.
    :param len_array: It's accept len_array as another parameter.
    :return: It's return the sorted array.
    """
    for current_index in range(len_array-1):
        for next_index in range(len_array-1-current_index):
            if array_[next_index] > array_[next_index+1]:
                array_[next_index], array_[next_index+1] = array_[next_index+1], array_[next_index]
    return array_


if __name__ == '__main__':
    try:
        size = int(input('Enter how many elements you want to enter : '))
        array = zeros(size, int)
        for index in range(size):
            print('Enter ', index+1, ' element: ', end='')
            array[index] = int(input())
        print('Sorted array is : ', bubble_sort(array, size))
    except ValueError as e:
        print('Enter integers only! Please try again...')
        logger.exception(e)
    except Exception as e:
        print('Oops! Something went wrong. Please try again...')
        logger.exception(e)
