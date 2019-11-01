"""
Equality check in python is done in two ways 
1. is
  Ex: a is b
  This type of comparision uses id(a) == id(b), i.e., idendity of the two objects
2. ==
  Ex: a == b
  __eq__ method is called by python

    hashable
    ===========
    -> The Fundamental Law of Hash (FLH) is this: objects that compare as equal have the 
        same hash value.
    -> An object is hashable if it has a hash value which never changes
    during its lifetime (it needs a __hash__() method), and can be
    compared to other objects (it needs an __eq__() method). Hashable
    objects which compare equal must have the same hash value.

    -> Hashability makes an object usable as a dictionary key and a set
    member, because these data structures use the hash value internally.

    -> All of Python's immutable built-in objects are hashable, while no mutable 
    containers (such as lists or dictionaries) are. Objects which are instances 
    of user-defined classes are hashable by default; they all compare unequal, 
    and their hash value is their id().

    -> If the hash method is not defined then the hash of the super class is used. 
        This is likely to result in the unexpected behavior.
        Ex: The default hash function of 'object' class uses id() function as value, so
        ultimately the hash value of the objects will be different
    -> When you define an __eq__ method for a class, remember to implement a __hash__ method or set __hash__ = None.
    -> The general idea about hashes is that if two objects have a different hash, they are not equal, but if they have the same hash, they might be equal
https://mail.python.org/pipermail/tutor/2011-September/085363.html
https://help.semmle.com/wiki/display/PYTHON/Inconsistent+equality+and+hashing
https://stackoverflow.com/questions/2909106/whats-a-correct-and-good-way-to-implement-hash

"""

class Jarvis(object):
    """
    Two hashable objects, if they compare equal, should have same hash value
    """

  def __init__(self, x=None):
    self.x = x

  def __eq__(self, other):
    print "EQUAL called"
    if type(self) == type(other):
      return self.x == other.x
    return False

  def __hash__(self):
    print "HASH CALLED..."
    # return True
    return hash(self.x)


a = Jarvis(x=1)
b = Jarvis(x=1)

print "id of object a ->", id(a)
print "id of object a ->", id(b)

# print "hash of object a ->", hash(a)
# print "hash of object b ->", hash(b)

print "a == b ->", a == b
print "a is b ->", a is b

print len(set([a, b]))

"""
If you don't want an object to be hashable then assign __hash__ to None
"""

class JarvisChild(Jarvis):
  __hash__ = None

print hash(JarvisChild())