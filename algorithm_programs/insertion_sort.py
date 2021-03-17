"""
Insertion Sort
Desc -> Reads in strings and prints them in sorted order using insertion sort.
I/P -> read in the list words
Logic -> Use Insertion Sort to sort the words in the String array
O/P -> Print the Sorted List
"""
from numpy import zeros
from logging_configuration import logging_config

logger = logging_config.get_logger()


def insertion_sort(array_, len_array):
    """
    This function sorted the array in ascending order.
    :param array_: It's accept array as a parameter.
    :param len_array: It's accept len_array as another parameter.
    :return: It's return the sorted array.
    """
    for current_index in range(1, len_array):
        key = array_[current_index]
        next_index = current_index - 1
        while next_index >= 0 and array_[next_index] > key:
            array_[next_index + 1] = array_[next_index]
            next_index -= 1
        array_[next_index + 1] = key
    return array_


if __name__ == '__main__':
    try:
        size = int(input('Enter how many elements you want to enter : '))
        array = zeros(size, int)
        for index in range(size):
            print('Enter ', index+1, ' element: ', end='')
            array[index] = int(input())
        sorted_array = insertion_sort(array, size)
        print('Sorted array is : ', sorted_array)
    except ValueError as e:
        print('Enter integers only! Please try again...')
        logger.exception(e)
    except Exception as e:
        print('Oops! Something went wrong. Please try again...')
        logger.exception(e)
