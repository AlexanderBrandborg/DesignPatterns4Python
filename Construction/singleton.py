# The classic singleton pattern. Now in Python!
# It's a bit wacky since we cannot protect the constructor
# Instead of accessing the singleton through a static method,
# we access it through dummy instances that are wrapped around it.
# (Usually I'd just implement singletonish behavior through a cached module,
#  but hey this gives us the possibility of doing some inheritance)
class Singleton(object):
    class __Singleton(object):
        path = "/some/nice/place/on/the/drive/"
    
    _instance = None

    def __init__(self):
        if not self._instance:
            self._instance = self.__Singleton()

    def __getattr__(self, name):
       return getattr(self._instance, name)
            

# Notice that they are different objects,
# but the getattr implementation allows us to access the internal singletons attributes
s = Singleton()
print(s)
print(s.path)

t = Singleton()
print(t)
print(t.path)

