# iterator = iter(range(5))
# print iterator.next()
# print iterator.next()
# print next(iterator)
# print dir(iterator)
# print type(iterator)
# print iterator.__next__()
# print "++++++++++++++++++++###########++++++++++++"
# file = open('Python.txt')
# print next(file)
# print file.next()
# print dir(file)
# print type(file)
# print file.__next__()

class MyIterator:
    # Old Style classes
# class MyIterator(object):
#     # New Style classes
    def __init__(self, *args, **kwargs):
        self.number = kwargs.get('number')

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        # __next__ is for Python 3
        # It is also useful if you manually iterate using obj = iter(MyIterator) and next(obj)
        if self.count > self.number:
            raise StopIteration
        count = self.count
        self.count = self.count + 1
        return "Fuckoff man, the Count is {0}".format(count)
    
    def next(self):
        # next is for Python 2
        if self.count > self.number:
            raise StopIteration
        count = self.count
        self.count = self.count + 1
        return "Fuckoff man, the Count is {0}".format(count)        

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# iterator = iter(MyIterator(number = 10))
# iterator = iter(PowTwo(10))
# print iterator.__next__()
# print iterator.__next__()
# print iterator.__next__()
# print iterator.__next__()

# for item in MyIterator(number = 10):
#     print item
############################################

class Iterator:
    # pass
    def __iter__(self):
        return self

    # def __next__(self):
    #     return 1

iterator_obj = iter(Iterator())


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        print "I am in iter method of {class_name} class".format(class_name=self.__class__)
        return RepeaterIterator(self)

class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def next(self):
        print "I am in next method of {class_name} class".format(class_name=self.__class__)
        return self.source.value

    def __next__(self):
        return self.source.value

obj = Repeater(26)
iterator_obj = iter(obj)
next(iterator_obj)