import abc
# Decorator pattern
# Allows us to transparently add new functionality to objects at run-time
# Basically we wrap one or more transparent objects around the object in question,
# which will then intercept calls made by the client
# This is a good way to get around a class explosion
# However, this pattern is not applicable if the ConcreteComponent is very heavyweight
# In this case we may end up with decorators that have a large number of 'transparent' methods. Wasteful.
# Given that, the strategy pattern would be a better choice.


class Component(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation(self):
        raise NotImplementedError

class ConcreteComponent(Component):
    def __init__(self, name):
        self._name = name

    def operation(self):
        return self._name

class Decorator(Component):
    def __init__(self, component):
        self._component = component
    
    def operation(self):
        return self._component.operation()

class CapitalDecorator(Decorator):
    def __init__(self, component):
        super().__init__(component)
    
    def operation(self):
        return super().operation().capitalize()

class GDDecorator(Decorator):
    def __init__(self, component):
        super().__init__(component)
    
    def operation(self):
        return 'God damn ' + super().operation() + '!'

cc = ConcreteComponent("bob sagat")
cd = CapitalDecorator(cc)
gdd = GDDecorator(cd)

print(gdd.operation())
