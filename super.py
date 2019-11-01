"""
    ########## super ##########
    What is super?
        Return a proxy object that delegates method calls to a parent or sibling class of type(parent)
    super(type) -> unbound super object
 |  super(type, obj) -> bound super object; requires isinstance(obj, type)
 |  super(type, type2) -> bound super object; requires issubclass(type2, type)
 
 -> super only works with 'type' but not 'classobj'
 -> Old style classes always creates 'classobj' i.e.,
        Ex: Class Parent:
                pass
            obj = Parent()
        In the above example Parent is 'classobj'(Everything is an object in python including classes)
            Ex: type(Parent)
            prints: <type 'classobj'>
-> New Style classes always creates 'type' objects
        Ex: class Parent(object):
                pass
            obj = Parent()
        In the above example class Parent is 'type' object (Everything is an object in python including classes)
            Ex: type(Parent)
            prints: <type 'type'>
-> When you try to call super with 'classobj'(created using old style classes), it raises "TypeError: super() argument 1 must be type, not classobj"
        Ex: class Parent:
                pass
            class Child(Parent):
                def __init__(self):
                    super(Child)
                    .....
            obj = Child()
        Result: 
            Traceback (most recent call last):
              File "super.py", line 20, in <module>
                obj = Child()
              File "super.py", line 16, in __init__
                obj = super(Child)
            TypeError: super() argument 1 must be type, not classobj
-> To use super with 'classobj', You need to convert 'classobj' to 'type' by using __metaclass__ attribute on any class
        Ex: Class Parent:
                __metaclass__ = type

            class Child(Parent):
                def __init__(self):
                    super(Child)
                    .....
            obj = Child()

************ 
1. objects / instances of a class can access the class attributes(properties and class methods) and everything inside the class(instance methods, instance attributes)
2. Class cannot access instance/objects attributes (methods and attributes), because whenever you call a instance method from class you need to provide a self(object itself)
Ex: 
class A(object):
    a = 1
    
    @classmethod
    def classmethod(cls):
        print cls, ".... I am class"
        print cls.__class__.__name__, ".... I am class"
        print cls.__name__, ".... I am class"

    def instancemehtod(self):
        print self, "----> instance method"
        print self.__class__, "----> instance method"
        print self.__class__.__name__, "----> instance method"

    @staticmethod
    def staticmethod():
        print "Hurray"

obj = A()
obj.a
obj.classmethod() -> python automatically add/inserts cls(Class itself attribute) to the classmethod
obj.instancemethod() - python automatically add/inserts self(object itself attribute) to the classmethod

A.classmethod()
A.a
A.instancemehtod - You can't call it, it will through an error because you need to add self which object itself


*************************

"""

class BaseClass(object):
# class BaseClass:
    # __metaclass__ = type

    # Instance method
    def first_method(self):
        pass

    @property
    def property_attribute(self):
        return "Property attribute"



class ChildClass(BaseClass):
    
    def __init__(self, *args, **kwargs):
        obj = super(ChildClass)
        obj_super = super(ChildClass, self)

obj_ = ChildClass()

############################ unbound super obj i.e., super(class) without super(class, obj) ############################

class A(object):
    a = 1
    def wow(self):
        return "Super"
class B(A):
    pass
class C(B):
    c = super(B)
    print c.a
    print c.wow
    #The above two lines gives error because
    # Directly acccesing super obj c(which is created without passing any object in to it(super)) gives errors,
    # because c is an unbound object i.e., you have created super class A's object by calling super(B) without any
    # instance / obj and so c cannot access any attributes of the parent class A


    def __init__(self):
        c_ = super(B)
        print c_
        # Directly acccesing super obj c_(which is created without passing any object in to it(super)) gives errors,
        # because c_ is an unbound object i.e., you have created super class A's object by calling super(B) without any
        # instance / obj and so c_ cannot access any attributes of the parent class A
        print c_.a
        print c_.wow

############################ converting unbound super obj i.e., super(class) to bound i.e, super(class, obj) ############################

class ParentClass(object):
     def f(self):
         return 1
     def __repr__(self):
         return '<instance of %s>' % self.__class__.__name__

class ChildClass(Parent): pass

#Unbound super objects must be turned into bound objects in order to make them to dispatch properly. 
#That can be done via the descriptor protocol. For instance, I can convert super(ChildClass) in a super object bound to child_obj in this way:
child_obj = ChildClass()
boundsuper = super(ChildClass).__get__(child_obj, ChildClass) # this is the same as super(ChildClass, child_obj)

#Now I can access the bound method ParentClass.f in this way:
print boundsuper.f
############################ ############################ 

# If you can't access the attributes of the super obj(which is unbound), then why do we need to create it and where it is used ?
# Below is the answer

obj = C()
print obj.c
print obj.c.a
print obj.c.wow
# The above statements converts obj.c.a calls super(C).__get__(obj,C).a which is turned into super(C, obj).a and retrieves A.a

#1. How to print super class / parent class name
#2. Why dir(obj) is not listing all the attributes of the obj
#3. Why unbound super obj cannot access the parent class(super obj) atrributes(methods/attributes), but can access super objects parent object(super' super object)
#4. What is unbound object
#5. What is bound object
#6. Why can't we access methods and attributes of unbound super object(super(A))
#7. How super class descriptor(__get__) works, how it binds unbound super object to bounded super object and returns values/attributes/results

print "####################################################################"
class A1(object):
    one = 1
    def one_method(self):
        return self.one # Searches for one in instance __dict__ first, if not found searches in A1 __dict__

class B1(A1):
    pass
    # def __get__(self, instance, instance_class_name_or_type):
    #     print "kjadkjsahdkjsahdkj"
    #     return object.__get__(instance, instance_class_name_or_type)

class C1(B1):
    # parent_of_b = B1
    parent_of_b = super(B1)
    print type(parent_of_b), "type(parent_of_b)"
    # print parent_of_b.one
    # print parent_of_b.one_method()

class D1(C1):
    pass

c_obj = C1()
print c_obj.parent_of_b.one, "== c_obj.parent_of_b.one"
print c_obj.parent_of_b.one_method(), "== c_obj.parent_of_b.one_method()"

d_obj = D1()
print d_obj.parent_of_b.one,"== d_obj.parent_of_b.one"
print d_obj.parent_of_b.one_method(), "== d_obj.parent_of_b.one"




