# 3. Power of 2
#    a. Desc -> This program takes a command-line argument N and prints
#       a table of the powers of 2 that are less than or equal to 2^N.
#    b. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int.
#    c. Logic -> repeat until i equals N.

from sys import argv
import logging

# implementing logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s : %(name)s : ', datefmt='%m/%d/%Y %I:%M:%S %p')
file_handler = logging.FileHandler('exceptions.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def power_of(num):
    """power_of(num): This function calculate the power of 2 of a number. It's adds all the values
       in a list. It returns a list."""
    _ = 0
    ls = []
    while _ != num:
        ls.append(2**_)
        _ += 1
    return ls


if __name__ == '__main__':
    try:
        N = int(argv[1])
        # validating the given condition
        if 0 <= N < 31:
            data = power_of(N)
            for val in data:
                print(val, ' ', end='')
        else:
            print('Please enter a integer(N) between 0 <= N <31 this range!')
    except Exception as e:
        logger.exception(e)
