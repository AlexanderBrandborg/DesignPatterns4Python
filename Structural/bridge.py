import abc
# Bridge pattern
# This allows us to seperate abstraction from implementation
# We have two hierachies, one of interfaces and one of implementations
# The alternative would be to have a single hierachy with nested generalizations. (A -> (B,C-> (D,E)).
# But with this pattern it could be a simple (A -> B -> C) hierachy with children pointing to implementations in the other hierachy.
# Compared to a single hierachy, abstraction and implementation hierachies do not need to evovle in tandem
# It also allows us to switch between implementations at runtime

class Abstraction(object, metaclass=abc.ABCMeta):
    _imp = None
    def __init__(self, implementor1, implementor2):
        self._imp1 = implementor1
        self._imp2 = implementor2
    
    @abc.abstractmethod
    def operation(self):
        raise NotImplementedError

class RefinedAbstraction(Abstraction):
    flag = True
    def __init__(self, implementor1, implementor2):
        super().__init__(implementor1, implementor2)
    
    def operation(self):
        if self.flag:
            self._imp1.operation()
        else:
            self._imp2.operation()

        self.flag = not self.flag


class VeryRefinedAbstraction(RefinedAbstraction):
    flag = True
    def __init__(self, implementor1, implementor2):
        super().__init__(implementor1, implementor2)
    
    def operation(self):
        if self.flag:
            self._imp2.operation()
        else:
            self._imp1.operation()

        self.flag = not self.flag


class Implementor(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation(self):
        raise NotImplementedError

class ConcreteImplementorA(Implementor):
    def operation(self):
        print("A Here!")

class ConcreteImplementorAChild(ConcreteImplementorA):
    def operation(self):
        print("AChild Here!")

# Client code
# Node that we are free to place whatever implementations we want into the absractions
# Without this we would have had to have more classes defined in the abstract hierachy for defining the different combinations of implementations submitted.
ra = RefinedAbstraction(ConcreteImplementorA(), ConcreteImplementorAChild())
ra.operation()
ra.operation()
ra.operation()
print('--------------')
vra = VeryRefinedAbstraction(ConcreteImplementorA(), ConcreteImplementorAChild())
vra.operation()
vra.operation()
vra.operation()