"""
Q. Binary Search the Word from Word List
    Desc -> Read in a list of words from File. Then prompt the user to enter a word to search the list.
     The program reports if the search word is found in the list.
    I/P -> read in the list words comma separated from a File and then enter the word to be searched
    Logic -> Use Arrays to sort the word list and then do the binary search
    O/P -> Print the result if the word is found or not
"""
from logging_configuration import logging_config

logger = logging_config.get_logger()

position = -1


def binary_search(word_list, item):
    """
    This function search the item by using binary_search algorithm.
    :param word_list: It's accept the word_list as a parameter.
    :param item: It's accept the item which we want to search.
    :return: It's return True & position if item found otherwise return False.
    """
    lower_bound = 0
    upper_bound = len(word_list) - 1
    while lower_bound <= upper_bound:
        mid_index = (lower_bound + upper_bound) // 2
        if word_list[mid_index] == item:
            globals()['position'] = mid_index
            return True
        else:
            if word_list[mid_index] < item:
                lower_bound = mid_index+1
            else:
                upper_bound = mid_index-1
    return False


if __name__ == '__main__':
    try:
        word_list_ = []
        size = int(input('Enter how many elements you want to store : '))
        for elements in range(size):
            print('Enter ', elements+1, ' element : ', end='')
            word_list_.append(input())
        word_list_ = sorted(word_list_)
        print('Sorted word list is : ', word_list_)
        item_ = input('Enter which element you want to search : ')
        if binary_search(word_list_, item_):
            print('Item found at position ', position+1)
        else:
            print('Item not found!')
    except Exception as e:
        print('Oops! Something went wrong!')
        logger.exception(e)
