"""
In Python you can create attributes of an object or a class as simple as 

class Hello(object):
    attr_1 = 'Wow'

obj = Hello()
obj.attr_2 = 'Wow 2'

But, we can manage(access, set value, delete the value/object itself) attributes, we have two ways
1. Descriptors - Most advanced way in python, Python uses descriptors underneath the covers to build properties, bound / unbound methods and class methods
2. property class(type) - property(fget, fset, fdel, "I'm the property.")
2. property decorators - Most widely used way - @property, @property.setter
"""
##############################
"""
Descriptors

1. Descriptors are used to create attributes and manage(access, set value, delete the value/object itself) them
2. When is it useful ?
    Ans : You want to assign an attribute to an object(instance of a class) and access to that attribute is carefully restrictable
          It is also useful to bound the method to an instance
"""
##############################

class DescriptorClass(object):
    def __init__(self): # __init__ can take any number of arguments
        self.name = ''

    def __get__(self, parent_instance, parent_class): # __get__ signature = __get__(self, instance, owner)
        print "\nInside __get__ method and returning name value\n"
        return self.name

    def __set__(self, instance, value): # __set__ signature = __set__(self, instance, value)
        print "\nInside __set__ method and setting name value as {} \n".format(value)
        self.name = value

    def __delete__(self, instance):
        del isinstance

# class Employee(object):
#     name = DescriptorClass(object) # creating an instance/object of DescriptorClass() and assiging to name attribute

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# employee_obj = Employee('Shiva', 30)
# print employee_obj.name

"""
When ever you acess employee_obj.name, python searches for 'name' attribute using LEGB (Local, Enclosed, Global, Built-in) rule
and in above class scenario it will find in class scope(E - Enclosed scope), and now python checks if that attribute is an object
or reference to an object and if it contains any one of the __get__, __set__, __del__ methods then python calls __get__ method with
the syntax - name.__get__(employee_obj, type(employee_obj))

There are two types of descriptors - 1. Data descriptors 2. Non Data descriptors
1. Data descriptors
    A class or object of a class having only __get__ method
2. Non Data descriptors
    A class or object of a class having both __get__ and __set__ methods

In Python, when you add a function inside a class, it is just a normal function, but it actually becomes a method when you access it as an attribute from object
as obj.attribute. This is because behind the scenes python class the __get__ method of function object and bound that method to object(instance of a class)

Ex : 
class Person:
    def superman(self):
        pass
obj = Person()
obj.superman() # Here function superman inside is basically a function object of type 'func' and this object has __get__ method inside it, so as stated above python checks
if that function object superman is descriptor i.e., if it has __get__ method, if so then calls the __get__ method as superman.__get__(obj, type(obj)) and now it becomes 
bounded method of 'obj' object
"""
# employee_obj.name = 'Shiva Krishna'
# print employee_obj.age

##############################
# property class(type) - property(fget, fset, fdel, "I'm the property.")
##############################

class Person(object):
    def __init__(self):
        self._name = ''
 
    def fget(self):
        print "Getting: %s" % self._name
        return self._name
     
    def fset(self, value):
        print "Setting: %s" % value
        self._name = value.title()
 
    def fdel(self):
        print "Deleting: %s" %self._name
        del self._name
    name = property(fget, fset, fdel, "I'm the property.")


user = Person()
user.name = 'john smith'
# Setting: john smith
user.name
# Getting: John Smith
# 'John Smith'
del user.name
# Deleting: John Smith

##############################
#property decorators - Most widely used way - @property, @property.setter, @property.deleter
##############################

class Person(object):
 
    def __init__(self):
        self._name = ''
 
    @property
    def name(self):
        print "Getting: %s" % self._name
        return self._name
 
    @name.setter
    def name(self, value):
        print "Setting: %s" % value
        self._name = value.title()
 
    @name.deleter
    def name(self):
        print ">Deleting: %s" % self._name
        del self._name

############################# Format one #############################

class Descriptor(object):
    def __get__(self, obj, type=None):
        print self
        # print self, type(self), obj, type(obj)
        print "<======== __get__ called ======>"

    def __set__(self, key, value):
        print "<======== __set__ called ======>"

    def __delete__(self, key, value):
        print "<======== __set__ called ======>"


class NewStyle(object):
    format_one = Descriptor()

    def __setattr__(self, key, value):
        print "<======== __setattr__ called ======>"

    def __delattr__(self, key):
        print "<======== __setattr__ called ======>"

    def __getattribute__(self, key):
        # print self, key
        # print type(self), key
        print "<======== __getattribute__ called ======>"
        return super(NewStyle, self).__getattribute__(key)

    def __getattr__(self, attr):
        print "<======== __getattr__ called ======>"
        self.__dict__[attr] = "Heman"
        return self.__dict__[attr]
        # return getattr(self, attr)

obj = NewStyle()
obj.format_one

# The concept is 
# __getattribute__ is called everytime for methods and calling signatures -  getattr, obj.attr, obj.__dict__['attr']
#   ------>  it means when an attribute of an object is accessed 
# __setattribute__ is called only when we try to assign an attribute to the object
# When you directly access __dict__ attribute to set a key, __setattribute__ is not called

class cached_property(object):
    """
    Decorator that converts a method with a single self argument into a
    property cached on the instance.

    Optional ``name`` argument allows you to make cached properties of other
    methods. (e.g.  url = cached_property(get_absolute_url, name='url') )
    """
    def __init__(self, func, name=None):
        print "Inside cached_property init method..."
        self.func = func
        self.__doc__ = getattr(func, '__doc__')
        self.name = name or func.__name__

    def __getattribute__(self, attr):
        # import ipdb; ipdb.set_trace()
        return super(cached_property, self).__getattribute__(attr)


    def __get__(self, instance, cls=None):
        print "Accessing __get__ method", instance, type(instance)
        if instance is None:
            return self
        try:
            instance.__dict__[self.name]
        except KeyError:
            print "AttributeError not found..."
        # res = instance.__dict__[self.name] = self
        return self


class HelloWorldClass(object):

    @cached_property
    def hello_world(self):
        return "Superman"

hellowrld_obj = HelloWorldClass()
# print ".............................."
# print hellowrld_obj.hello_world, "--->One"
# print ".............................."
# print hellowrld_obj.hello_world, "--->Two"

print ">>>>>>>>>>"
class property_vs_classdescriptor(object):
    """
    property object code executes everytime you 
    accessed the property attribute object
    like obj.something
    """
    call_count  = 0

    def __getattr__(self, attr):
        import ipdb; ipdb.set_trace()

    def __getattribute__(self, attr):
        # import ipdb; ipdb.set_trace()
        return super(property_vs_classdescriptor, self).__getattribute__(attr)

    @property
    def something(self):
        self.call_count += 1
        print "Something is called for <<'{}'>> times".format(self.call_count)
        return 2*3

pr_obj = property_vs_classdescriptor()
print pr_obj.something, "-------ONe"
print pr_obj.something, "-------TWo"
print pr_obj.something, "-------Three"
print getattr(pr_obj, 'something')