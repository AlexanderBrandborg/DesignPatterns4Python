import copy
import abc
# The prototype pattern is often used in the same places as the abstract factory
# However it does not limit us to create families of objects within factories

# With prototyping, we can compose an object with whatever prototypes we want without the family concept.
# Here, a prototype is just an object instance that can be cloned.


class CoinPrototype(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def clone(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def getWeight(self):
        raise NotImplementedError


class Silver(CoinPrototype):
    _weight = 5
    def clone(self):
        return copy.deepcopy(self)
    
    def getWeight(self):
        return self._weight

    def __str__(self):
        return "Silver"


class Gold(CoinPrototype):
    _weight = 10
    def clone(self):
        return copy.deepcopy(self)
    
    def getWeight(self):
        return self._weight

    def __str__(self):
        return "Gold"


class MaterialPrototype(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def clone(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def can_hold_weight(self, weight):
        raise NotImplementedError


class Canvas(MaterialPrototype):
    _weight_limit = 20

    def clone(self):
        return copy.deepcopy(self)
    
    def can_hold_weight(self, weight):
        return weight < self._weight_limit

    def __str__(self):
        return "Canvas"


class Leather(MaterialPrototype):
    _weight_limit = 40

    def clone(self):
        return copy.deepcopy(self)
    
    def can_hold_weight(self, weight):
        return weight < self._weight_limit
        
    def __str__(self):
        return "Leather"
    

class MagicBag(object):
    stamina = 0
    weapon_prototype = None
    coins = []
    def __init__(self, material_prototype, coin_prototype):
        self.material_prototype = material_prototype
        self.coin_prototype = coin_prototype

    def _total_weight(self):
        result = 0
        for coin in self.coins:
            result += coin.getWeight()
        return result


    def add_coins(self, number):
        for x in range(number):
            if self.material_prototype.can_hold_weight(self._total_weight()):
                self.coins.append(self.coin_prototype.clone())
            else:
                self.coins = []
                print(str(self.material_prototype) + " Bag Broke")
                break

    def inspect_bag(self):
        print(str(self.material_prototype) + " Bag contains " + str(len(self.coins)) + ' ' + str(self.coin_prototype) + ' Coins.')


# Here's the client code
# By using prototyping here, we can create 4 types of magic bag, which can spawn new objects as well.
# This is done without a rigid class inheritancer system
# Each prototype we add would require more classes to be defined
# Especially if those classes would be very simple that would be wasteful
bag = MagicBag(Leather(), Silver())
bag.add_coins(2)
bag.inspect_bag()
bag.add_coins(1)