"""
    Facade Design Pattern

    This pattern involves an interface which acts as a bridge which makes the functionality of  concrete
    classes independent from interface implementer classes. Both types of classes can be altered structurally
    without affecting each other.
"""
from abc import ABC, abstractmethod


class Implementor(ABC):
    @abstractmethod
    def is_on_state(self):
        pass

    @abstractmethod
    def is_off_state(self):
        pass


class Sensor(Implementor):
    def __init__(self):
        pass

    def is_on_state(self):
        print('Sensor is ON')

    def is_off_state(self):
        print('Sensor is OFF')


class Smoke(Implementor):
    def __init__(self):
        pass

    def is_on_state(self):
        print('Smoke is ON')

    def is_off_state(self):
        print('Smoke is OFF')


class Light(Implementor):
    def __init__(self):
        pass

    def is_on_state(self):
        print('Light is ON')

    def is_off_state(self):
        print('Light is OFF')


class Facade:
    def __init__(self):
        self._sensor = Sensor()
        self._smoke = Smoke()
        self._light = Light()

    def emergency(self):
        self._sensor.is_on_state()
        self._smoke.is_on_state()
        self._light.is_on_state()

    def no_emergency(self):
        self._sensor.is_off_state()
        self._smoke.is_off_state()
        self._light.is_off_state()


if __name__ == '__main__':
    facade = Facade()
    sensor = 28
    if sensor > 30:
        facade.emergency()
    else:
        facade.no_emergency()
