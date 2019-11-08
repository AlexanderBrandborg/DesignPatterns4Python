import abc
# Command pattern
# Treats commands as first class citizens in our code
# A command knows it receiver that it enacts requests upon, but the calling invoker does not know what receiver is being interacted with by executing a command.
# This creates a loose coupling between invoker and receiver.
# Commands can be switched out at runtime, and at the same time they can implement undo functionality
# Logging Command objects executed, we should be able to repeat old actions as well

class Command(object, metaclass=abc.ABCMeta):
    _receiver = None
    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        raise NotImplementedError

class ConcreteCommand(Command):
    def execute(self):
        self._receiver.action()

class Receiver(object):
    def action(self):
        print("I did an action!")

class Receiver2(object):
    def action(self):
        print("I did another action!")

class Invoker(object):
    _command = None
    def __init__(self, command):
        self._command = command
    
    def poke(self):
        self._command.execute()

r = Receiver()
cc = ConcreteCommand(r)
invoker = Invoker(cc)
invoker.poke()

r2 = Receiver2()
cc = ConcreteCommand(r2)
invoker = Invoker(cc)
invoker.poke()