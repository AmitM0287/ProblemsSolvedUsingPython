"""
Q. An Anagram Detection Example
    Desc -> One string is an anagram of another if the second is simply a rearrangement of the first.
    For example, 'heart' and 'earth' are anagrams...
    I/P -> Take 2 Strings as Input such abcd and dcba and Check for Anagrams
    O/P -> The Two Strings are Anagram or not....
"""
from logging_configuration import logging_config

logger = logging_config.get_logger()


def check_anagram(string1, string2):
    """
    This function accept two string & then compare each other for anagram or not.
    :param string1: It's accept string1 as a parameter.
    :param string2: It's accept string2 as a parameter.
    :return: It's return True if strings are anagram each other otherwise False.
    """
    if len(string1) != len(string2):
        return False
    string1 = sorted(string1)
    string2 = sorted(string2)
    if string1 == string2:
        return True
    return False


if __name__ == '__main__':
    try:
        string_1 = input('Enter a string : ')
        string_2 = input('Enter another string : ')
        if check_anagram(string_1, string_2):
            print('The Two Strings are Anagram')
        else:
            print('The Two Strings are not Anagram')
    except Exception as e:
        print('Oops! Something went wrong. Please try again...')
        logger.exception(e)
