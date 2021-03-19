"""
Palindrome-Checker
Desc -> A palindrome is a string that reads the same forward and backward, for example,
 radar, toot, and madam. We would like to construct an algorithm to input a string of
  characters and check whether it is a palindrome.
I/P -> Take a String as an Input
Logic -> The solution to this problem will use a deque to store the characters of the string.
 We will process the string from left to right and add each character to the rear of the deque.
O/P -> True or False to Show if the String is Palindrome or not.
"""
from logging_configuration import logging_config

logger = logging_config.get_logger()


def is_palindrome(string_):
    """
    This function check weather a string is palindrome or not.
    :param string_: It's accept a string as a parameter.
    :return: It's return True if the string is palindrome otherwise Fasle
    """
    reverse = ''
    for char in string_:
        reverse = char + reverse
    if string_.capitalize() == reverse.capitalize():
        return True
    else:
        return False


if __name__ == '__main__':
    try:
        string = input('Enter a string : ')
        if is_palindrome(string):
            print(string, ' is a palindromic string.')
        else:
            print(string, ' is not a palindromic string.')
    except Exception as e:
        print('Oops! Something went wrong. Please try again.')
        logger.exception(e)
