import abc
# Template Method
# This pattern is used when we want to vary parts of an algorithm.
# In the abstract case we define the overall structure of the algorithm,
# but we allow our children to plug in the missing parts of the algorithm.
# Thus we seperate algorithm structure and low-level implementation. (Less code duplicaiton)

class AbstractClass(object, metaclass=abc.ABCMeta):
    def template_method(self, val):
        return val - (self.primitive_operation_1() + self.primitive_operation_2())
        
    @abc.abstractmethod
    def primitive_operation_1(self):
        NotImplementedError
    
    @abc.abstractmethod
    def primitive_operation_2(self):
        NotImplementedError


class ConcreteClass(AbstractClass):
    def primitive_operation_1(self):
        return 5
    
    def primitive_operation_2(self):
        return 2

cc = ConcreteClass()
print(cc.template_method(9))