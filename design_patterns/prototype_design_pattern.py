"""
    Prototype Design Pattern

    The Prototype design pattern is good for when creating new objects requires more resources than
    you want to use or have available. You can save resources by just creating a copy of any existing
    object that is already in memory.
    E.g., A file you’ve downloaded from a server may be large, but since it is already in memory,
    you could just clone it, and work on the new copy independently of the original.
"""
from abc import ABCMeta, abstractmethod


class IProtoType(metaclass=ABCMeta):
    """interface with clone method"""
    @abstractmethod
    def clone(self):
        pass


class Prototype(IProtoType):
    """A Concrete Class"""
    def __init__(self, field):
        self.field = field

    def clone(self):
        """"This clone method uses a shallow copy technique """
        return type(self)(self.field)

    def __str__(self):
        return f"{id(self)}\tfield={self.field}\ttype={type(self.field)}"


if __name__ == '__main__':
    # Creates object containing a list
    object1 = Prototype([1, 207, 3, 4])
    print(f"OBJECT1 {object1}")
    # Clone
    object2 = object1.clone()
    # Change the value of one of the list elements in OBJECT2,
    # to see if it also modifies the list element in OBJECT1.
    # If it changed OBJECT1s copy also, then the clone was done
    object2.field[1] = 101
    # Comparing OBJECT1 and OBJECT2
    print(f"OBJECT2 {object2}")
    print(f"OBJECT1 {object1}")
