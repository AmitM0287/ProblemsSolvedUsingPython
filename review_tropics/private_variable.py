"""
In actual terms (practically), python doesn't have anything called private member variable in Python.
However, adding two underlines(__) at the beginning makes a variable or a method private is the convention
used by most python code.
"""


class Human:
    # private variable
    __height = 6
    # private method
    def __do_something(self):
        print('I am coding now.')


if __name__ == '__main__':
    man = Human()
    print(man.__height)
    man.__do_something()
