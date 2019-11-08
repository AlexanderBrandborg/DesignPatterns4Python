import abc
# Good old composite pattern
# This is used when we want to create a hierachy of instances that contain other instances,
# but we want to operate on all instances somewhat equally

# Here the composite instances can contain other composites or leafs
# All implement the operation method, where the composite will be sure to
# call the same method on all its childred

# Note that some methods are not implemented on Leaf as that does not make sense.
# They throw errors for the sake of safety, but they kinda need to be there 
# so that Composites and Leafs can be treated in a similar way

class Component(object):
    def operation(self):
        raise NotImplementedError

    def add(self, child):
        raise NotImplementedError

    def remove(self, child):
        raise NotImplementedError

    def get_child(self, index):
        raise NotImplementedError

class Composite(Component):
    def __init__(self):
        self._children = []

    def operation(self):
        result = '|'
        result += ','.join([child.operation() for child in self._children])
        result += '|'
        return result
    
    def add(self, child):
        self._children.append(child)
    
    def remove(self, child):
        self._children.remove(child)

    def get_child(self, index):
        self._children[index]

class Leaf(Component):
    def operation(self):
        return 'leaf'

c1 = Composite()
c1.add(Leaf())
c1.add(Leaf())

c2 = Composite()
c2.add(Leaf())
c2.add(c1)

print(c2.operation())