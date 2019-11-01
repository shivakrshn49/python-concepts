############################ function based ###################
import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        print func.__name__, "##########"
        return func().upper()
    return wrapper


@uppercase
def greet():
    """Return a friendly greeting."""
    return 'Hello!'


if __name__ == '__main__':
    print greet()


######################### class based #############################
class ClassBasedDecorator(object):

    def __init__(self, func_to_decorate):
        print "INIT ClassBasedDecorator"
        self.func_to_decorate = func_to_decorate

    def __call__(self, *args, **kwargs):
        print "CALL ClassBasedDecorator"
        return self.func_to_decorate(*args, **kwargs)


@ClassBasedDecorator
def print_moar_args(*args):
    for arg in args:
        print arg

print type(print_moar_args)
print isinstance(print_moar_args, ClassBasedDecorator)

class ClassBasedDecoratorWithParams(object):

    def __init__(self, arg1, arg2):
        print "*********************"
        print "INIT ClassBasedDecoratorWithParams"
        print arg1
        print arg2
        print "*********************"

    def __call__(self, fn):
        # print fn, "Does python passed this?"
        print "CALL ClassBasedDecoratorWithParams"
        # print self, fn, args, kwargs, "**************"

        def new_func(*args, **kwargs):
            print "Function has been decorated.  Congratulations."
            return fn(*args, **kwargs)
        return new_func


@ClassBasedDecoratorWithParams("arg1", "arg2")
def print_args_again(*args):
    for arg in args:
        print arg


# print_args_again(1, 2, 3)
# print_args_again(1, 2, 3)

