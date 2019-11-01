
# 1,2,3,4,5,6

def natural_numbers(n):
    if n<=1:
        return n
    else:
        return n + natural_numbers(n-1)

# print natural_numbers(25)


class LearningREPR(object):
    def __init__(self, *args, **kwargs):
        pass

obj = LearningREPR()
# print type(obj).__name__
# print obj

# new_obj = eval(repr(obj))
# print new_obj