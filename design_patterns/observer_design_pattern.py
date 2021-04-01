"""
    Observer Design Pattern

    The observer design is a Behavioral design Pattern which allows you to define or create
    a subscription mechanism to send the notification to the multiple objects about any new
    event that happens to the object that they are observing. The subject is basically
    observed by multiple objects. The subject needs to be monitored and whenever there is
    a change in the subject, the observers are being notified about the change.

    This pattern defines one to Many dependencies between objects so that one object changes
    state, all of its dependents are notified and updated automatically.
"""
from abc import ABC, abstractmethod


class Implementor(ABC):
    @abstractmethod
    def register(self, who):
        pass

    @abstractmethod
    def unregister(self, who):
        pass

    @abstractmethod
    def dispatch(self, msg):
        pass


class Publisher(Implementor):
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, msg):
        for subscriber in self.subscribers:
            subscriber.update(msg)


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, msg):
        print('{} got message "{}"'.format(self.name, msg))


if __name__ == '__main__':
    publisher = Publisher()
    # Subscribers
    Bob = Subscriber('Bob')
    Alice = Subscriber('Alice')
    John = Subscriber('John')
    # Register
    publisher.register(Bob)
    publisher.register(Alice)
    publisher.register(John)
    # Dispatch & Unregister
    publisher.dispatch('It is Lunch Time')
    publisher.unregister(John)
    publisher.dispatch('Time for Dinner')
