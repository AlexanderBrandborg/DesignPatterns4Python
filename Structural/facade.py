# The Facade Pattern
# Creates an interface object in front of a subsystem to make a common access for that subsystem
# This makes use easier for users and at the same time it more weakly couples the system
# Now the client code only has to worry about the Facade, so we can update the subsystem of 
# complex classes in whatever way we want as long as we update the guts of the Facade.

class Facade(object):
    def __init__(self):
        self._complex1 = ComplexClass()
        self._complex2 = ComplexClass2()

    def operation1(self):
        self._complex1.operation()
    
    def operation2(self):
        self._complex2.operation()

# Users will not have to care about this implementation
class ComplexClass(object):
    def operation(self):
        print('Complex Operation 1!')

class ComplexClass2(object):
    def operation(self):
        print('Complex Operation 2!')


f = Facade()
f.operation1()
f.operation2()