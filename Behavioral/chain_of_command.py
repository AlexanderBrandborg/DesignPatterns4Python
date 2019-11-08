import abc
# Chain of command pattern
# We sometimes need to send requests to one or more objects.
# The naive implementation would require all objects to know about each other.
# A right mess
# Instead each object gets a successor in a chain of objects.
# When a request is sent on, what happens depends on the objects in the rest of the chain.
# This also allows us to change request behavior at run-time by changing the chain.

class Handler(object):
    _successor = None

    def __init__(self, successor):
        self._successor = successor

    def handle_request(self):
        if self._successor:
            self._successor.handle_request()

class ConcreteHandler(Handler):
    def handle_request(self):
        print("Concrete Touched!")
        super().handle_request()

class DumbHandler(Handler):
    pass      


small_chain = DumbHandler(ConcreteHandler(None))
small_chain.handle_request()

print ("-------------")
big_chain = ConcreteHandler(DumbHandler(ConcreteHandler(ConcreteHandler(DumbHandler(None)))))
big_chain.handle_request()
