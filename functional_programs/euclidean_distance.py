"""
3. Write a program that takes two integer command-line arguments x and y
   and prints the Euclidean distance from the point (x, y) to the origin (0, 0).
   The formula to calculate distance = sqrt(x*x + y*y).
"""
from sys import argv
from math import sqrt
from logging_configuration import logging_config

logger = logging_config.get_logger()


def euclidean_distance_of(point_a, point_b):
    """
    This function calculates the euclidean distance from the point (point_a, point_b) to the origin (0, 0).
    :param point_a: It's accept point_a as a argument.
    :param point_b: It's accept point_b as another argument.
    :return: It's return the euclidean distance.
    """
    result = point_a*point_a + point_b*point_b
    return sqrt(result)


if __name__ == '__main__':
    try:
        # taking inputs from command line
        point_x, point_y = int(argv[1]), int(argv[2])
        # store the result
        distance = euclidean_distance_of(point_x, point_y)
        print('The euclidean distance from the point (', point_x, ', ', point_y, ') to origin (0, 0) is : ', distance)
    except Exception as e:
        logger.exception(e)
