"""
1. Any Class that has __enter__, __exit__ methods defined is nothing but a Context Manager Class / Context Manager
2. with statement/identifier/keyword only works on instances of Context Manager Classes or functions
3. Context Manager Class are used to acquire and close the system resources efficiently like file opening etc.,
4. You can create Context managers in three ways 
    1. Implementing __enter__, __exit__ methods in the class
    2. 'contextmanager' decorator from contextlib module - from contextlib import contextmanager
    3. Python 3 - Inheriting 'ContextDecorator' from contextlib module - from contextlib import ContextDecorator
"""
#################################### method 1 ######################
class ContextManager(object):

    def __init__(self, name):
        print "I entered __init__ method"
        self.name = name

    def __enter__(self):
        print "I entered __enter__ method"
        # import ipdb; ipdb.set_trace()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "I entered __exit__ method"
        print self, exc_type, exc_val, exc_tb
        # import ipdb; ipdb.set_trace()


if __name__ == '__main__':

    with ContextManager(name='with') as context_manager_instance:
        print "I am in ContextManager body"
        print context_manager_instance
        # raise ValueError('sadsada')

#################################### method 2 ######################
from contextlib import contextmanager

@contextmanager
def managed_file(name):
    print "I am enter"
    yield "Super"
    print "I am exit"

if __name__ == '__main__':
    with managed_file("Wow") as f:
        print f

#################################### method 3 - Python 3######################
"""
from contextlib import ContextDecorator

class ManagerFile(ContextDecorator):
    def __enter__(self):
        print "I am enter"
        return self

    def __exit__(self):
        print "I am exit"

with ManagerFile("Wow") as f:
    print f
    print "I am in body"
"""


############################################################Task / Excercise############################################################
########################################################################################################################

print """ ######### Find the execution time of a programm ######### """

import time
from contextlib import contextmanager
######## 1. contextmanager function

@contextmanager
def find_program_execution_time(seconds):
    start_time = time.time()
    print start_time, "----> Starting time"
    list_ = []
    for i in range(7):
        list_.append(i)
        time.sleep(seconds)
    end_time = time.time() 
    print end_time, "----> Ending time"
    execution_time = end_time - start_time
    yield execution_time
    print execution_time, "----> Execution time"

if __name__ == '__main__':
    with find_program_execution_time(1) as execution_time_object:
        print execution_time_object, "------> Resulting time"
        print type(execution_time_object)




######## 2. Custom class

class ContextManager(object):

    def __enter__(self):
        self.start_time = time.time()
        print self.start_time, "----> Starting time"
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print self.end_time, "----> Ending time"
        self.result_time = self.end_time - self.start_time
        print self.result_time, "----> Resulting time"


if __name__ == '__main__':
    with ContextManager() as context_manager_object:
        print context_manager_object, "------> context_manager_object"
        print type(context_manager_object)

import dis
def wow():
    print 'Wow'
    return 'Wow'

dis.dis(ContextManager)