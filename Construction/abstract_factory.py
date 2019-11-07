import abc
# The Benefits of the Abstract Factory Pattern, as shown in this file are:
# 1. It helps us to switch out what objects are used by an application
# 2. It collects together objects that need to be used together (our building and pet)
# A possible downside here is that adding new factory "products" requires updates in many parts of code

class PropertyFactory(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_pet(self):
        raise NotImplementedError

    @abc.abstractmethod
    def create_building(self):
        raise NotImplementedError


class FarmFactory(PropertyFactory):
    def create_pet(self):
        return Cow()
    def create_building(self):
        return FarmHouse()


class HomesteadFactory(PropertyFactory):
    def create_pet(self):
        return Cat()

    def create_building(self):
        return Shack()


class AbstractPet(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def make_noise(self):
        raise NotImplementedError


class Cow(AbstractPet):
    def make_noise(self):
        print("Moo")


class Cat(AbstractPet):
    def make_noise(self):
        print("Miaw")


class AbstractBuilding(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_value(self):
        raise NotImplementedError


class FarmHouse(AbstractBuilding):
    def get_value(self):
        return 10000


class Shack(AbstractBuilding):
    def get_value(self):
        return 100


# This represents other part of the application that just needs to use
# the objects created by the factory.
def application(factory):
    pet = factory.create_pet()
    pet.make_noise()
    building = factory.create_building()
    print(building.get_value())

# Here we select which factory to use for the application
# Notice the easy switching :- )
factory = HomesteadFactory()
application(factory)