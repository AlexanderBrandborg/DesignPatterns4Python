import abc
# The builder pattern is used when we need to construct complex objects.
# It splits code that constructs the object parts(Builder), from the code that directs the assembly of the object(Constructor). 
# By defining an abstract Builder, we can easily write new code for constructing a different type of object,
# while the director stays the same. It also encapsulates the constructing and representing code.

class Director(object):
    builder = None
    def __init__(self, builder):
        self.builder = builder
    
    def construct(self, string):
        for char in string:
            if char.isdigit():
                self.builder.build_digit(char)
            elif char.isalpha():
                self.builder.build_letter(char)
            else:
                self.builder.build_other(char)



class Builder(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def build_digit(self, element):
        raise NotImplementedError

    @abc.abstractmethod
    def build_letter(self, element):
        raise NotImplementedError

    @abc.abstractmethod
    def build_other(self, element):
        raise NotImplementedError


class Repeater(Builder):
    result = ""
    def build_digit(self, element):
        self.result += element
    def build_letter(self, element):
        self.result += element
    def build_other(self, element):
        self.result += element
    
    def get_repeater_string(self):
        return self.result

class NumberExtracter(Builder):
    result = ""
    def build_digit(self, element):
        self.result += element
    def build_letter(self, element):
        pass
    def build_other(self, element):
        pass

    def get_number_string(self):
        return self.result

# This is the client codee that creates a director and feeds it a 
# a builder object to construct and object from the provided data
# Here both builders create strings, but they could create any object needed.
r = NumberExtracter()
d = Director(r)
d.construct("1jlk234ljkl;;;")
print(r.get_number_string())