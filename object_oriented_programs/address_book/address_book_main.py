"""
The software can be used to maintain an address book. An address book holds a collection of entries,
each recording a person's first and last names, address, city, state, zip and phone number.
"""
from logging_configuration import logging_config

# set up logger to handle exceptions
from object_oriented_programs.address_book.AddressBook import AddressBook

logger = logging_config.get_logger()


def welcome_screen(user_):
    """
    This method is used to display the operations that can be perform by that user.
    :param user_: It's accept user as a parameter.
    :return: None
    """
    option = 'y'
    while option == 'y':
        print('\n______________Welcome To Address Book______________\n')
        option = int(input('1. Insert Details \n2. Update Details \n3. Delete Details \n4. Quit \n\n'
                           'You chosen option : '))
        if option == 1:
            user_.insert_data()
        elif option == 2:
            option = int(input('\nChoose which data you want to update : \n1. First Name \n2. Last Name \n3. Address '
                               '\n4. City \n5. State \n6. Pin Code \n7. Phone Number \n\nYou Chosen option : '))
            user_.update_data(option)
        elif option == 3:
            option = int(input('\nChoose which data you want to Delete : \n1. First Name \n2. Last Name \n3. Address '
                               '\n4. City \n5. State \n6. Pin Code \n7. Phone Number \n\nYou Chosen option : '))
            user_.delete_data(option)
        elif option == 4:
            exit()
        else:
            print('Wrong Input! Try Again...\n\n')
            welcome_screen(user_)
        option = input('\nDo you want to continue (y/n) : ')


if __name__ == '__main__':
    user = AddressBook()
    try:
        welcome_screen(user)
    except ValueError as e:
        print('Enter integers only !')
        logger.exception(e)
        welcome_screen(user)
    except Exception as e:
        print('\nOops! Something went wrong! Try again...\n')
        logger.exception(e)
        welcome_screen(user)
