"""
Q. User Input and Replace String Template “Hello <<UserName>>, How are you?”
    a. I/P -> Take User Name as Input. Ensure UserName has min 3 char
    b. Logic -> Replace <<UserName>> with the proper name
    c. O/P -> Print the String with User Name
"""
from logging_configuration import logging_config

logger = logging_config.get_logger()


def is_valid(user_name):
    """
    This function check weather the username is valid or not. If it has the minimum length 3 then it's valid.
    :param user_name: It's take user_name as a parameter.
    :return:  It's return True if user_name is valid, otherwise return False.
    """
    if len(user_name) >= 3:
        return True
    else:
        return False


def replace_by(string_, username_):
    """
    This function replace the existing sting_ with the username_.
    :param string_: It's accept a string_ as a parameter.
    :param username_: It's accept username_ as another parameter.
    :return: It's return the updated sting_ by replacing the username_.
    """
    # convert string to list
    list_ = list(string_.split(' '))
    list_[1] = username_+','
    # convert list to string
    updated_string_ = ' '
    return updated_string_.join(list_)


if __name__ == '__main__':
    try:
        string = 'Hello <<UserName>>, How are you?'
        username = input('Enter username : ')
        # check weather username is valid or not
        if is_valid(username):
            updated_string = replace_by(string, username)
            print(updated_string)
        else:
            print('Username should has minimum 3 character! Please try again...')
    except Exception as e:
        print('Oops! Something went wrong! Please try again...')
        logger.exception(e)
