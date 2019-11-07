# This is the object-based adapter pattern
# It allows us to take an outside class 'StrangeCreature' with a different interface,
# and squeeze that SOB into another hierachy.
# The good thing about the object version of this pattern is that if StrangeCreature had
# a lot of subtypes, we would not need to write an adapter for each subtype.
#(I don't think this is relevant considering Pythons Dynamic Typing, but it's good to know for something like C++ I'm guessing)

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

class Platypus(Animal):
    _strange_creature = None
    def __init__(self):
        self._strange_creature = StrangeCreature()
    
    def make_noise(self):
        return self._strange_creature.make_horrible_noise()

p = Platypus()
p.make_noise()

h = Horse()
h.make_noise()