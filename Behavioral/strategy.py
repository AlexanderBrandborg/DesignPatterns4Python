import abc
# Strategy pattern
# This allows us to change the algorithm used by a class by giving it as a parameter
# This seperates the complex algorithm code form the rest of the class and allows for run-time switching
# It helps us avoid creating a lot of new classes that only differ in their algorithm

class Strategy(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def process(self, l):
        raise NotImplementedError

class DumbStrategy(Strategy):
    def process(self, l):
        return l

class SorterStrategy(Strategy):
    def process(self, l):
        return list(sorted(l))

class ListPrinter():
    def __init__(self, strategy):
        self._strategy = strategy
    
    def print_list(self, list):
        print(self._strategy.process(list))

lp = ListPrinter(DumbStrategy())
lp.print_list([3, 2, 1])

lp = ListPrinter(SorterStrategy())
lp.print_list([3, 2, 1])