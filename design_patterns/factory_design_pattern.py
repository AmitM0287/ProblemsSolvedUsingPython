"""
    Factory Design Pattern

    Whenever you have no idea about the number of objects or classes. Let say you have two class A & B. And
    in the future you might need a class C. I fwe use inheritance so, there many things we have to change.
    So, there is a better way to do this to use a design pattern to gets the objects.
"""


class A(object):
    def __init__(self):
        pass

    def method_A(self):
        print('I am method A')


class B(object):
    def __init__(self):
        pass

    def method_B(self):
        print('I am method B')


def get(obj=''):
    objs = dict(a=A(), b=B())
    return objs[obj]


if __name__ == '__main__':
    a = get('a')
    a.method_A()
    b = get('b')
    b.method_B()
