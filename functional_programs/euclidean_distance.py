# 3. Write a program that takes two integer command-line arguments x and y
#    and prints the Euclidean distance from the point (x, y) to the origin (0, 0).
#    The formula to calculate distance = sqrt(x*x + y*y).

from sys import argv
from math import sqrt
import logging

# Implementing logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s : %(name)s : ', datefmt='%m/%d/%Y %I:%M:%S %p')
file_handler = logging.FileHandler('exceptions.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def euclidean_distance_of(a, b):
    """euclidean_distance_of(a, b): This function calculates the euclidean distance from
       from the point (a, b) to the origin (0, 0)."""
    res = a*a + b*b
    return sqrt(res)


if __name__ == '__main__':
    try:
        # taking inputs from command line
        x, y = int(argv[1]), int(argv[2])
        # store the result
        dis = euclidean_distance_of(x, y)
        print('The euclidean distance from the point (', x, ', ', y, ') to origin (0, 0) is : ', round(dis, 4))
    except Exception as e:
        logger.exception(e)
