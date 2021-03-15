"""
5. Write a program that takes two float command-line arguments t and v and prints the wind chill.
   Use Math.pow(a, b) to compute ab. Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour),
   the National Weather Service defines the effective temperature (the wind chill) to be:
   Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger
   than 120 or less than 3 (you may assume that the values you get are in that range).
   w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*v^0.16
"""

from sys import argv
from math import pow
from logging_configuration import logging_config

logger = logging_config.get_logger()


def calc_windchill(temperature_, wind_speed_):
    """
    This function calculate the wind_chill(w) value. Formula :
    wind_chill = 35.74 + 0.6215*temperature_ + (0.4275*temperature_ - 35.75)*wind_speed_^0.16
    The formula is not valid if temperature_ is larger than 50 in absolute value or if wind_speed
    is larger than 120 or less than 3.
    :param wind_speed_: It's accept wind_speed_ as a argument.
    :param temperature_: It's accept temperature_ as another argument.
    :return: It's return the wind_chill value.
    """
    wind_chill_ = 35.74 + 0.6215*temperature_ + (0.4275*temperature_ - 35.75)*pow(wind_speed_, 0.16)
    return wind_chill_


if __name__ == '__main__':
    try:
        # taking the value of t and v from command-line argument
        temperature, wind_speed = float(argv[1]), float(argv[2])
        # the formula is not valid if t is larger than 50
        if temperature > 50.0:
            print('Temperature must be less than 50')
        # the formula is not valid if v is larger than 120 or less than 3
        elif wind_speed < 3 or wind_speed > 120:
            print('Wind_speed must be less than 120 or greater than 3')
        else:
            wind_chill = calc_windchill(temperature, wind_speed)
            print('Wind chill value : ', wind_chill)
    except ValueError as e:
        print('Enter integer numbers only! Please try again...')
        logger.exception(e)
    except Exception as e:
        print('Oops! Something went wrong! Please try again...')
        logger.exception(e)
