class ValueTooSmallError(Exception):
    pass


class ValueTooLargeError(Exception):
    pass


if __name__ == '__main__':
    try:
        value = 10
        number = int(input('Enter a number : '))
        if number < value:
            raise ValueTooSmallError
        elif number > value:
            raise ValueTooLargeError
        else:
            print('You guess the right number!')
    except ValueTooSmallError:
        print('This value is too small. Try again...')
    except ValueTooLargeError:
        print('This value is too large. Try again...')
