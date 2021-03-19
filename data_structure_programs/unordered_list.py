"""
UnOrdered List
Desc -> Read the Text from a file, split it into words and arrange it as Linked List.
Take a user input to search a Word in the List. If the Word is not found then add it
 to the list, and if it found then remove the word from the List. In the end save the list into a file
I/P -> Read from file the list of Words and take user input to search a Text
Logic -> Create a Unordered Linked List. The Basic Building Block is the Node Object.
 Each node object must hold at least two pieces of information. One ref to the data field
 and  second the ref to the next node object.
O/P -> The List of Words to a File.

"""
from logging_configuration import logging_config

logger = logging_config.get_logger()


def is_found(new_word):
    """
    This function find the new_word is present or not into the file.
    :param new_word: It's accept new_word as a parameter.
    :return: It's return a list of word.
    """
    file = open('words.txt', mode='r')
    list_of_words = []
    for word in file.read().split(' '):
        list_of_words.append(word)
    file.close()
    # initialized found by False
    found = False
    for word in list_of_words:
        if word == new_word:
            list_of_words.remove(new_word)
            found = True
    if not found:
        list_of_words.append(new_word)
    return list_of_words


def update_file(list_of_words):
    """
    This function update the file.
    :param list_of_words: It's accept list of words.
    :return: None
    """
    file = open('words.txt', mode='w')
    for word in list_of_words:
        word = word + ' '
        file.write(word)
    file.close()


if __name__ == '__main__':
    try:
        new_word_ = input('Enter a word : ')
        list_of_words_ = is_found(new_word_)
        update_file(list_of_words_)
    except Exception as e:
        print('Oops! Something went wrong! Please try again!')
        logger.exception(e)
