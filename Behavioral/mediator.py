import abc

# Mediator Pattern
# In the case that we have a section of objects that are communicating a lot, we risk everyone being coupled together with everyone.
# This makes it harder to switch out objects, and make updates. New medidation will have to be done through subclassing of individual classes.
# Mediator pattern allows us instead to push all mediation between classes into a single object. 
# Objects only communicate with the mediator, and it will in turn determine what objects to call on a requests.
# It is easy to update object interaction as it requires only the mediator to be subclassed
# Of course the mediator risks becoming very complex :- )

class Mediator(object, metaclass=abc.ABCMeta):
    def __init__(self):
        self._colleauges = []

    def register(self, colleauge):
        self._colleauges.append(colleauge)

    @abc.abstractmethod
    def poke_all(self):
        raise NotImplementedError


class ConcreteMediator(Mediator):
    def poke_all(self):
        for c in self._colleauges:
            c.poke()


class Colleauge(object, metaclass=abc.ABCMeta):
    def __init__(self, mediator):
        self._mediator = mediator 
        self._mediator.register(self)

    def poke_colleauges(self):
        self._mediator.poke_all()
    
    @abc.abstractmethod
    def poke(self):
        raise NotImplementedError
        

class ConcreteColleauge1(Colleauge):
    def poke(self):
        print("ConcreteType1 was poked!")

class ConcreteColleauge2(Colleauge):
    def poke(self):
        print("ConcreteType2 was poked!")


cm = ConcreteMediator()
colleauges = [ConcreteColleauge1(cm), ConcreteColleauge2(cm), ConcreteColleauge1(cm), ConcreteColleauge2(cm)]

colleauges[0].poke_colleauges()
