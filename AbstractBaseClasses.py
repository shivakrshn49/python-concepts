"""
Inheritance does not force to implement a method, for example AbstractBaseClass has 
a first_method, now when LearnAbstractBaseClass inherits AbstractBaseClass, then it
just acquires all the parent attributes(methods, properties), but if we did not 
implement first_method in LearnAbstractBaseClass, no error will be raised
So if you want to raise an error if LearnAbstractBaseClass not implemented all the 
methods in parent class AbstractBaseClass, then we should use abstract base classes 
"""

# from abc module
# class AbstractBaseClass(object):
#     def first_method(self):
#         raise NotImplementedError

# class LearnAbstractBaseClass(AbstractBaseClass):
#     pass

# obj = LearnAbstractBaseClass()
# obj.first_method()

#######################################################################
#Inheritance
#__metaclass___ (can be used in python 2 syntax)
#metaclass=somemetaclass (This syntax will be used in Python 3)
#ParentClass.register(ChildClass)
#######################################################################

#We can convert above class in to Abstract Class by using python's __metaclass__ attribute

import abc


class AbstractBaseClass(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def first_method(self):
        pass

    @abc.abstractproperty
    def value(self):
        return 'Should never get here'

#Two ways to use the above abstract class

# one
class LearnAbstractBaseClass(AbstractBaseClass):
    def first_method(self):
        print "Hello"

    @property
    def value(self):
        return ""

    # def value(self):
    #     pass

#Two
AbstractBaseClass.register(LearnAbstractBaseClass)


obj = LearnAbstractBaseClass()
print dir(obj), "-----Dir"
print vars(obj), "-----vars"
print type(obj.value)
print LearnAbstractBaseClass.__bases__

from abc import ABCMeta, abstractmethod

class Metaclass(type):
    pass

# class Base(ABCMeta):
class Base(object):
    __metaclass__ = ABCMeta
    # __metaclass__ = Metaclass
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
# class Concrete(object):
    # __metaclass__ = Metaclass
    def foo(self):
        pass



