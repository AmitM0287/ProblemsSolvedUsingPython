"""
    Singleton Design Pattern

    This design pattern restricts programmer to create multiple instances. It's make sure that you
    can only create one and only one instance.


    class A(object):
    def __init__(self):
        pass


    if __name__ == '__main__':
        obj = A()
        print(obj)
        # < __main__.A object at 0x000001B733FEA7C0 >
        obj2 = A()
        print(obj2)
        # < __main__.A object at 0x000001B734017C70 >

"""


class MetaClass(type):
    """
        This is singleton design pattern
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
            If instance already exist don't create
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instances[cls]
        return cls._instances[cls]


class Singleton(metaclass=MetaClass):
    def __init__(self):
        pass


if __name__ == '__main__':
    object1 = Singleton()
    print(object1)
    object2 = Singleton()
    print(object2)
    object3 = Singleton()
    print(object3)
