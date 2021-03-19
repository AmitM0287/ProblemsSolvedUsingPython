"""
Protected variables are those data members of a class that can be accessed within the class and
the classes derived from that class. In Python, there is no existence of “Public” instance variables.
 However, we use underscore ‘_’ symbol to determine the access control of a data member in a class.
"""


class Lenovo:
    # protected variable
    _price = 28700
    # protected method
    def _configuration(self):
        print('RAM: 8GB  ROM: 2TB  Gen: 8')


if __name__ == '__main__':
    laptop = Lenovo()
    print(laptop._price)
    laptop._configuration()
