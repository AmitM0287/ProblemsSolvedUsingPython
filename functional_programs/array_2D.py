"""
1. 2D Array
   a. Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from standard input
      and printing them out to standard output.
   b. I/P -> M rows, N Cols, and M * N inputs for 2D Array.
   c. Logic -> create 2 dimensional array in memory to read in M rows and N cols
   d. O/P -> Print function to print 2 Dimensional Array.
"""
from numpy import zeros
from logging_configuration import logging_config

logger = logging_config.get_logger()


def get_datatype():
    """
    This function helps user to choose one data types from below-
       1. Integer  2. Float  3. Boolean
    :return: It's return that data type which is chosen by user.
    """
    choice = int(input('Please choose a datatype : \n 1. Integer \n 2. Float \n 3. Boolean \n You choose : '))
    if choice == 1:
        return int
    elif choice == 2:
        return float
    elif choice == 3:
        return bool
    else:
        print('You chosen wrong input!')
        exit()


if __name__ == '__main__':
    try:
        row = int(input('Enter Row number : '))
        col = int(input('Enter Column number : '))
        d_type = get_datatype()
        arr = zeros((row, col), d_type)
        # taking inputs from user
        for i in range(row):
            for j in range(col):
                print('Enter value for (', i, ',', j, ') position : ', end='')
                arr[i][j] = eval(input())
        # print the array
        print('Your 2D array is : ')
        for i in range(row):
            for j in range(col):
                print(arr[i][j], ' ', end='')
            print()
    except ValueError as e:
        print('Enter integer numbers only! Please try again...')
        logger.exception(e)
    except Exception as e:
        print('Oops! Something went wrong! Please try again...')
        logger.exception(e)
