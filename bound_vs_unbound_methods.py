#https://stackoverflow.com/questions/13348031/python-bound-and-unbound-method-object
#Whenever you look up a method via instance.name (and in Python 2, class.name), the method object is created a-new. 
#Python uses the descriptor protocol to wrap the function in a method object each time.

#So, when you look up id(C.foo), a new method object is created, you retrieve its id (a memory address), 
#then discard the method object again. Then you look up id(cobj.foo), a new method object created that re-uses the now freed memory 
#address and you see the same value. The method is then, again, discarded (garbage collected as the reference count drops to 0).

#Next, you stored a reference to the C.foo unbound method in a variable. Now the memory address is not freed 
#(the reference count is 1, instead of 0), and you create a second method instance by looking up cobj.foo which has to use a new memory 
#location. Thus you get two different values.

#Two objects with non-overlapping lifetimes may have the same id() value python

class D(object):

    def f(self, x):
        return x

    def g(self, x):
        return x

d = D()
print D.__dict__['f'], id(D.__dict__['f'])
print D.f, id(D.f), '<<<D.f'
print d.f, id(d.f), '<<<d.f'
print '*************'
# print D.__dict__['g'], id(D.__dict__['g'])
# print D.g, id(D.g), '<<<D.g'
# print d.g, id(d.g), '<<<d.g'
# print '**************'

assigned = d.f
again_assigned = D.f
print id(assigned)
print id(again_assigned)
print d.f, id(d.f), '<<<d.f<<<<<<'
print D.f, id(D.f), '<<<D.f'

# print [id(x) for x in (d.f, d.f, D.f, D.f)]
