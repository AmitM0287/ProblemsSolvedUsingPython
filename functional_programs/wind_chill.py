# 5. Write a program that takes two float command-line arguments t and v and prints the wind chill.
#    Use Math.pow(a, b) to compute ab. Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour),
#    the National Weather Service defines the effective temperature (the wind chill) to be:
#    Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger
#    than 120 or less than 3 (you may assume that the values you get are in that range).
#    w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*v^0.16

from sys import argv
from math import pow
import logging

# Implementing logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s : %(name)s : ', datefmt='%m/%d/%Y %I:%M:%S %p')
file_handler = logging.FileHandler('exceptions.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def calc_windchill(t_, v_):
    """calc_windchill(t_, v_): This function calculate the wind_chill(w) value. Formula :
       w_ = 35.74 + 0.6215*t + (0.4275*t - 35.75)*v^0.16
       The formula is not valid if t_ is larger than 50 in absolute value or if v_ is larger
       than 120 or less than 3. It return the wind chill value.
       """
    w_ = 35.74 + 0.6215*t_ + (0.4275*t_ - 35.75)*pow(v_, 0.16)
    return w_


if __name__ == '__main__':
    try:
        # taking the value of t and v from command-line argument
        t, v = float(argv[1]), float(argv[2])
        # the formula is not valid if t is larger than 50
        if t > 50.0:
            print('t must be less than 50')
        # the formula is not valid if v is larger than 120 or less than 3
        elif v < 3 or v > 120:
            print('v must be less than 120 or greater than 3')
        else:
            w = calc_windchill(t, v)
            print('Wind chill value : ', w)
    except Exception as e:
        logger.exception(e)
