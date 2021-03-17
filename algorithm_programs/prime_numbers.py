"""
Take a range of 0 - 1000 Numbers and find the Prime numbers in that range.
Extend the above program to find the prime numbers that are Anagram and Palindrome
"""
from logging_configuration import logging_config

logger = logging_config.get_logger()


def is_prime_number(number_):
    """
    This function calculate a number is prime number or not.
    :param number_: It's accept a integer number as argument.
    :return: It's return True if it's a prime number otherwise False.
    """
    flag = 0
    for values in range(2, number_//2):
        if number_ % values == 0:
            flag += 1
    if flag == 1:
        return True
    else:
        return False


def is_palindrome(number_):
    """
    This function calculates the number is palindrome or not.
    :param number_: It's accept a number as a parameter.
    :return: It's return True if it's a Palindrome number otherwise False.
    """
    temp = number_
    reverse = 0
    while number_ > 0:
        digit = number_ % 10
        reverse = reverse * 10 + digit
        number_ = number_ // 10
    if temp == reverse:
        return True
    else:
        return False


if __name__ == '__main__':
    try:
        number = int(input('Enter the range to gets all the prime numbers: '))
        print('Prime Numbers are : ')
        for numbers in range(2, number+1):
            if is_prime_number(numbers):
                print(numbers, ' ', end='')
        print('\nPrime Numbers which are Palindrome: ')
        for numbers in range(2, number+1):
            if is_prime_number(numbers):
                if is_palindrome(numbers):
                    print(numbers, ' ', end='')
    except ValueError as e:
        print('Inputs should be an Integer Number! Try Again...')
        logger.exception(e)
    except Exception as e:
        print('Oops! Something went wrong! Try Again...')
        logger.exception(e)
