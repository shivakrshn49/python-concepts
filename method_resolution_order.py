import os

################Python 3.X################

# class Animal:
#   def __init__(self, animalName):
#     print(animalName, 'is an animal.');

# class Mammal(Animal):
#   def __init__(self, mammalName):
#     print(mammalName, 'is a warm-blooded animal.')
#     super().__init__(mammalName)
    
# class NonWingedMammal(Mammal):
#   def __init__(self, NonWingedMammalName):
#     print(NonWingedMammalName, "can't fly.")
#     super().__init__(NonWingedMammalName)

# class NonMarineMammal(Mammal):
#   def __init__(self, NonMarineMammalName):
#     print(NonMarineMammalName, "can't swim.")
#     super().__init__(NonMarineMammalName)

# class Dog(NonMarineMammal, NonWingedMammal):
#   def __init__(self):
#     print('Dog has 4 legs.');
#     super().__init__('Dog')
    
# d = Dog()
# print('')
# bat = NonMarineMammal('Bat') 

################Python 2.X################
#**********New Style Classes**********
print "**********New Style Classes**********"
class Animal(object):
  def __init__(self, animalName):
    print(animalName, 'is an animal.');

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super(Mammal, self).__init__(mammalName)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammalName):
    print(NonWingedMammalName, "can't fly.")
    super(NonWingedMammal, self).__init__(NonWingedMammalName)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammalName):
    print(NonMarineMammalName, "can't swim.")
    super(NonMarineMammal, self).__init__(NonMarineMammalName)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super(Dog, self).__init__('Dog')

print Dog.__mro__
#The mro for old style classes is
#(<class '__main__.Dog'>, <class '__main__.NonMarineMammal'>, <class '__main__.NonWingedMammal'>, <class '__main__.Mammal'>, <class '__main__.Animal'>, <type 'object'>)
# If you call super manually, python will execute all the inherited class for sure
# If python interpretter calls it, if it finds in the first inherited method then it executes that method and stops there

d = Dog()
print('')
# print(os.system('python -V'))
bat = NonMarineMammal('Bat') 

#**********Old Style Classes**********
print "**********Old Style Classes**********"

class Animal:
  pass
  # def __init__(self, animalName):
  #   print(animalName, 'is an animal.');

class Mammal(Animal):
  pass
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammalName):
    print(NonWingedMammalName, "can't fly.")

class NonMarineMammal(Mammal):
  pass
  def __init__(self, NonMarineMammalName):
    print(NonMarineMammalName, "can't swim.")

class Dog(NonMarineMammal, NonWingedMammal):
  pass
  def __init__(self):
    print('Dog has 4 legs.');


obj = Dog()
# obj = Dog("Dog")
#The mro for old style classes is
#(<class '__main__.Dog'>, <class '__main__.NonMarineMammal'>, <class '__main__.Mammal'>, <class '__main__.Animal'>, <class '__main__.NonWingedMammal'>, <type 'object'>)


################################ Diamond Problem ###############################
print '****************'
#http://www.lambdafaq.org/what-about-the-diamond-problem/
#https://stackoverflow.com/questions/1848474/method-resolution-order-mro-in-new-style-classes
# class A(object):
class A:
  pass
  # print "I am in class A"
  # def m1(self):
  #   print "I am in class A"

class B(A):
  pass
  # print "I am in class B"
  # def m1(self):
  #   print "I am in class B"

class C(A):
  pass
  # print "I am in class C"
  # def m1(self):
  #   print "I am in class C"

class D(B, C):
  pass
  # print "I am in class D"
  # def m1(self):
  #   print "I am in class D"

# D_object = D()
# D_object.m1()

# New Style MRO
#-------------------------
"D - B - C - A"

#Old Style MRO
#-------------------------
"D - B - A - C - A"

print "#########################################################"

class ParentParent1(object):
    attribute = 1

class ParentParent2(object):
    attribute = 1

class Parent1(ParentParent1):
    attribute = 1

class Parent2(ParentParent2):
    attribute = 1

class ParentChildA(Parent1):
    pass

class ParentChildB(Parent2):
    pass

class ParentChildAB(ParentChildA, ParentChildB):
    pass


obj_ = ParentChildAB()
print ParentChildAB.__mro__
print obj_.attribute