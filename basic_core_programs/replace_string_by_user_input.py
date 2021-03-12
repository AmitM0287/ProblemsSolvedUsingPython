# 1. User Input and Replace String Template “Hello <<UserName>>, How are you?”
#    a. I/P -> Take User Name as Input. Ensure UserName has min 3 char
#    b. Logic -> Replace <<UserName>> with the proper name
#    c. O/P -> Print the String with User Name

import logging

# implementing logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s : %(name)s : ', datefmt='%m/%d/%Y %I:%M:S %p')
file_handler = logging.FileHandler('exceptions.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def is_valid(username):
    """is_valid(username): This function check weather the username is valid or not.
       If it has the minimum length 3 then it's valid & return True otherwise return False."""
    if len(username) >= 3:
        return True
    else:
        return False


def replace_by(uname_, new_uname_):
    """replace_by(uname_, new_uname_): This function replace the existing username with the new one.
       It returns the new sting by replacing the username."""
    # Convert string to list
    ls = list(uname_.split(' '))
    ls[1] = new_uname_+','
    # Convert list to string
    st = ' '
    return st.join(ls)


if __name__ == '__main__':
    try:
        uname = 'Hello <<UserName>>, How are you?'
        new_uname = input('Enter a valid Username : ')
        # Check weather username is valid or not.
        if is_valid(new_uname):
            s = replace_by(uname, new_uname)
            print(s)
        else:
            print('UserName must has minimum 3 character')
    except Exception as e:
        logger.exception(e)
