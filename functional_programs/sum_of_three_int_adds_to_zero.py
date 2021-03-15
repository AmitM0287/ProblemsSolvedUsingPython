"""
2. Sum of three Integer adds to ZERO
   a. Desc -> A program with cubic running time. Read in N integers and counts the
      number of triples that sum to exactly 0.
   b. I/P -> N number of integer, and N integer input array
   c. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
   d. O/P -> One Output is number of distinct triplets as well as the second output is to print the distinct triplets.
"""
from numpy import zeros
from logging_configuration import logging_config

logger = logging_config.get_logger()


def find_triplets(array_, len_of_array):
    """
    This function calculate the triplets of sum zero.
    :param array_: It's accept array as a argument.
    :param len_of_array: It's accept len_of_array as a argument.
    :return: It returns a list of triplets of sum equals to zero.
    """
    list_ = []
    found = False
    for i in range(0, len_of_array-2):
        for j in range(i+1, len_of_array-1):
            for k in range(j+1, len_of_array):
                if array_[i] + array_[j] + array_[k] == 0:
                    list_.extend([array_[i], array_[j], array_[k]])
                    found = True
    if not found:
        print("Triplets of sum zeros doesn't exist")
        exit()
    else:
        return list_


def separate(triplet_):
    """
    This function adds a separator(';') in the list of triplets of sum zero.
    :param triplet_: It's accept triplet_ as a argument.
    :return: It's return a list of triplets of sum zero with a separator(;).
    """
    index_ = 3
    while index_ < len(triplet_):
        triplet_.insert(index_, ';')
        index_ += 4
    return triplet_


if __name__ == '__main__':
    try:
        # taking the length of array from user
        len_array = int(input('Enter how many elements you want to enter to get a triplet of sum zero : '))
        # define array
        array = zeros(len_array, int)
        # taking user inputs from user
        for index in range(len_array):
            print('Enter ', (index+1), ' element : ', end='')
            array[index] = int(input())
        # check triplets of sum equals to zero
        triplet = find_triplets(array, len_array)
        len_triplet = len(triplet)
        # print the triplets
        print('Total ', len_triplet // 3, ' triplets found of sum zero!')
        # separate triplets
        triplets = separate(triplet)
        # print all the triplets of sum zero
        for item in triplets:
            print(item, ' ', end='')
    except ValueError as e:
        print('Enter integer numbers only! Please try again...')
        logger.exception(e)
    except Exception as e:
        print('Oops! Something went wrong! Please try again...')
        logger.exception(e)
