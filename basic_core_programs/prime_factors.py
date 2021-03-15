"""
Q. Factors
   a. Desc -> Computes the prime factorization of N using brute force.
   b. I/P -> Number to find the prime factors
   c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
   d. O/P -> Print the prime factors of number N.
"""
from math import sqrt
from logging_configuration import logging_config

logger = logging_config.get_logger()


def prime_factors_of(number_):
    """
    This function calculate the prime factors of a number. It's add all the prime factors in a list.
    :param number_: It's accept a number_ as a parameter.
    :return: It's return the list of prime factors.
    """
    list_of_prime_factors = []
    # add the number of two's that divide number_ in the list
    while number_ % 2 == 0:
        list_of_prime_factors.append(2)
        number_ = number_ / 2
    # number_ must be odd at this point
    for factors_ in range(3, int(sqrt(number_)) + 1, 2):
        while number_ % factors_ == 0:
            list_of_prime_factors.append(factors_)
            number_ = number_ / factors_
    # number_ should be a prime number if greater than 2
    if number_ > 2:
        list_of_prime_factors.append(int(number_))
    return list_of_prime_factors


if __name__ == '__main__':
    try:
        number = int(input("Enter a number to get it's prime factors : "))
        if number > 0:
            prime_factors_list = prime_factors_of(number)
            print('Prime factors of ', number, ' are : ', end='')
            for prime_factor in prime_factors_list:
                print(prime_factor, ' ', end='')
        else:
            print('Enter positive integer only! Please try again...')
    except ValueError as e:
        print('Enter integers only! Please try again...')
        logger.exception(e)
    except Exception as e:
        print('Oops! Something went wrong! Please try again...')
        logger.exception(e)
