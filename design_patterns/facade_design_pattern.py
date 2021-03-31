"""
    Facade Design Pattern

    This pattern involves an interface which acts as a bridge which makes the functionality of  concrete
    classes independent from interface implementer classes. Both types of classes can be altered structurally
    without affecting each other.
"""


class Sensor(object):
    def __init__(self):
        pass

    def sensor_on(self):
        print('Sensor is ON')

    def sensor_off(self):
        print('Sensor OFF')


class Smoke(object):
    def __init__(self):
        pass

    def smoke_on(self):
        print('Smoke ON')

    def smoke_off(self):
        print('Smoke OFF')


class Light(object):
    def __init__(self):
        pass

    def light_on(self):
        print('Light ON')

    def light_off(self):
        print('Light OFF')


class Facade(object):
    def __init__(self):
        self._sensor = Sensor()
        self._smoke = Smoke()
        self._light = Light()

    def emergency(self):
        self._sensor.sensor_on()
        self._smoke.smoke_on()
        self._light.light_on()

    def no_emergency(self):
        self._sensor.sensor_off()
        self._smoke.smoke_off()
        self._light.light_off()


if __name__ == '__main__':
    facade = Facade()
    sensor = 28
    if sensor > 30:
        facade.emergency()
    else:
        facade.no_emergency()
