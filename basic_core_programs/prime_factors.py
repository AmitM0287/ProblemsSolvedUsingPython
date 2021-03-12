# 6. Factors
#   a. Desc -> Computes the prime factorization of N using brute force.
#   b. I/P -> Number to find the prime factors
#   c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
#   d. O/P -> Print the prime factors of number N.

from math import sqrt
import logging

# implementing logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s : %(name)s : ', datefmt='%m/%d/%Y %I:%M:S %p')
file_handler = logging.FileHandler('exceptions.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def prime_factors(num_):
    """prime_factors(num_): This function calculate the prime factors of a integer.
       It's add all the prime factors in a list. It returns the list of prime factors."""
    ls = []
    # add the number of two's that divide num_ in the list
    while num_ % 2 == 0:
        ls.append(2)
        num_ = num_ / 2
    # num_ must be odd at this point
    for item_ in range(3, int(sqrt(num_)) + 1, 2):
        while num_ % item_ == 0:
            ls.append(item_)
            num_ = num_ / item_
    # num_ must be a prime number if greater than 2
    if num_ > 2:
        ls.append(int(num_))
    return ls


if __name__ == '__main__':
    try:
        num = int(input("Enter a number to get it's prime factors : "))
        if num > 0:
            factors = prime_factors(num)
            print('Prime factors of ', num, ' are : ', end='')
            for item in factors:
                print(item, ' ', end='')
        else:
            print('Please enter a positive integer')
    except Exception as e:
        logger.exception(e)
