def generator():
    yield 'Fuck'
    yield 'Off'

generator_obj = generator()
# print generator_obj.next()
# print generator_obj.next()
# print next(generator_obj)
# print next(generator_obj)
#########################################
def generator_two(range_=None):
    range_ = range_
    for i in range_:
        pass

def iterator(value):
    for i in range(value):
        print i

one = iterator(5)
print one
print type(one)
print "#################################"

def generator(value):
    for i in range(value):
        print i, "Hahahah"
        yield i

two = generator(5)
# print two
# print type(two)
# next(two)
# next(two)

object_1 = None
