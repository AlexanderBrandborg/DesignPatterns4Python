# Proxy pattern.
# Creates a transparent object in front of an actual subject.
# In this example, it is used to defer instantiation of the actual subject as it is slow.
# However it could also be used if the subject is in another address space, but we want to treat it,
# as if it is here in our code space. Could require some network calls.
# Could also be a protection proxy that checks whether clients are allowed to call as certain object
# Think of this pattern to replace pointers to objects, if we want those pointers to do something extra.

import abc

class Subject(object, metaclass=abc.ABCMeta):
    _size = 10
    def get_size(self):
        return self._size

    @abc.abstractmethod
    def request(self):
        raise NotImplementedError

class Proxy(Subject):
    _real_subject = None
    def request(self):
        self._real_subject = RealSubject()
        self._real_subject.request()

class RealSubject(Subject):
    def request(self):
        print("Wow, I'm doing a really heavy operation here!")


p = Proxy()

# We can ask about the object, without actually instantiating the actual subject 
print(p.get_size())

# This could require something like a file load or a network call, which would be slow
# Especially if we have a lot of these objects and the application, tries to load them at once
p.request()
