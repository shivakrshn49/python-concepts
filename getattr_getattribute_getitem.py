print """
Concept is :
Whenever/everytime you tried to access an attribute of an object
__getattribute__ will gets called.

This magic method will first search the attribute in object's __dict__
method, if it founds then returns it, if it does not found then it calls
__getattr__ magic method to search the attribute for, if it still does not
found then raises AttributeError
"""

class ParentClass(object):
    a1 = 5

    def method_one(self):
        print "I am in ParentClass method_one"
        return "Hello"

    def __getattr__(self, attr):
        # import ipdb; ipdb.set_trace()
        print "I am in  method __getattr__, and you searched for '%s'"%attr
        self.__dict__[attr] = attr
        print self.__dict__, "{{{{}}}}}}}}"
        # return self.__dict__[attr]
        # return attr
        # return 'You searched for %s ,  but i have given you a big hahah'%attr
        # return 'You searched for %s ,  but i have given you a big hahah'%attr
        return attr


    # def __getattribute__(self, attr):
    #     print "I am in ParentClass class __getattribute__ and got attribute as '%s'"%attr
    #     print super(ParentClass, self).__getattribute__(attr), '--> Actual __dict__ in super'
    #     return super(ParentClass, self).__getattribute__(attr)

    def __getitem__(self, attr):
        print "I am in ParentClass class __getitem__"
        return super(ParentClass, self).__getitem__(attr)

parentObject = ParentClass()
print parentObject.everyone

class ChildClass(ParentClass):

    a2 = 6

    def method_two(self):
        print "I am in ChildClass method_two"

    # def __getattr__(self, attr):
    #     print "I am in ChildClass class __getattr__, and you searched for '%s'"%attr
    #     # self.__dict__[attr] = attr
    #     print self.__dict__
    #     # return self.__dict__[attr]
    #     # return attr
    #     # return 'hahah'

    # def __getattribute__(self, attr):
    #     print "I am in ChildClass class __getattribute__ and got attribute as '%s'"%attr
    #     return super(ChildClass, self).__getattribute__(attr)

    def __getitem__(self, attr):
        print "I am in ChildClass class __getitem__"
        return super(ChildClass, self).__getitem__(attr)


obj = ChildClass()
# import ipdb; ipdb.set_trace()
print obj.wow, ">>>>>>> Priting outside of class"
print obj['unknown']


