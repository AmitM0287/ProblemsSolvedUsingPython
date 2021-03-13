"""
Q. Leap Year
   a. I/P -> Year, ensure it is a 4 digit number.
   b. Logic -> Determine if it is a Leap Year.
   c. O/P -> Print the year is a Leap Year or not.
"""
from logging_configuration import logging_config

logger = logging_config.get_logger()


def is_leap_year(year_):
    """
    is_leap_year(year_): This function check weather a year is leap year or not.
    If that year is a leap year then it returns True otherwise it returns False.
    """
    if year_ % 4 == 0:
        if year_ % 100 == 0:
            if year_ % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    try:
        year = input('Enter a year : ')
        if len(year) == 4:
            if is_leap_year(int(year)):
                print(year, ' is a Leap Year')
            else:
                print(year, ' is not a leap year')
        else:
            print('Enter year of 4 digits! Please try again...')
    except ValueError:
        print('A year must be an integer! Please try again...')
    except Exception as e:
        print('Oops! Something went wrong! Please try again...')
        logger.exception(e)
