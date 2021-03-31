"""
    Factory Design Pattern

    Whenever you have no idea about the number of objects or classes. Let say you have two class A & B. And
    in the future you might need a class C. I fwe use inheritance so, there many things we have to change.
    So, there is a better way to do this to use a design pattern to gets the objects.
"""
from abc import ABC, abstractmethod


class Implementor(ABC):
    @abstractmethod
    def who_am_i(self):
        pass


class Computer(Implementor):
    def __init__(self):
        pass

    def who_am_i(self):
        print('I am Computer.')


class Television(Implementor):
    def __init__(self):
        pass

    def who_am_i(self):
        print('I am Television')


class Factory:
    def __init__(self):
        pass

    def get_instance_of(self, obj=''):
        instance = dict(Computer=Computer(), Television=Television())
        return instance[obj]


if __name__ == '__main__':
    factory = Factory()
    computer = factory.get_instance_of('Computer')
    computer.who_am_i()
    television = factory.get_instance_of('Television')
    television.who_am_i()
