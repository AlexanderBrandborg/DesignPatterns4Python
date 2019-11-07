# This is the class-based adapter pattern
# It allows us to take an outside class 'StrangeCreature' with a different interface,
# and squeeze that SOB into another hierachy.
# It uses multiple inheritance, but in this simple case it is easier to do than using the object adapter.

import abc

class StrangeCreature(object):
    def make_horrible_noise(self):
        print("Rawr")

class Animal(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def make_noise(self):
        raise NotImplementedError

class Horse(Animal):
    def make_noise(self):
        print("Vrinsk")

class Platypus(Animal, StrangeCreature):
    def __init__(self):
        self._strange_creature = StrangeCreature()
    
    def make_noise(self):
        return self.make_horrible_noise()

p = Platypus()
p.make_noise()

h = Horse()
h.make_noise()