import abc
# Observer pattern
# Used when a change in state of one object requires changes to other object. But we don't know how many there will be
# Allows us to notify an 'unlimited' number of observers
# Makes a loose coupling between subject and observers

class Subject(object):
    _observers = []

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detatch(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for o in self._observers:
            o.update(self)


class ConcreteSubject(Subject):
    _value = 0
    def get_state(self):
        return self._value

    def set_state(self, value):
        self._value = value
        self.notify()

class Observer(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self):
        raise NotImplementedError

class ConcreteObserver(Observer):
    def __init__(self, name):
        self._name = name
        self._total = 0

    def update(self, subject):
        self._total += subject.get_state()
        print(self._name + ":Total increased to: " + str(self._total)) 
        

co1 = ConcreteObserver("Bob")
co2 = ConcreteObserver("Alice")

cs = ConcreteSubject()
cs.attach(co1)
cs.attach(co2)

cs.set_state(5)
cs.set_state(6)
