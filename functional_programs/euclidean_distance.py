# 3. Write a program that takes two integer command-line arguments x and y
#    and prints the Euclidean distance from the point (x, y) to the origin (0, 0).
#    The formula to calculate distance = sqrt(x*x + y*y).

from sys import argv
from math import sqrt


# calculate euclidean distance
def distance_bet(a, b):
    res = a*a + b*b
    return sqrt(res)


if __name__ == '__main__':
    try:
        # taking inputs from command line
        x, y = int(argv[1]), int(argv[2])
        # store the result
        dis = distance_bet(x, y)
        print('The euclidean distance from the point (', x, ', ', y, ') to origin (0, 0) is : ', round(dis, 4))
    except Exception as e:
        print(e)
