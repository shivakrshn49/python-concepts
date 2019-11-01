class Car:
 
    _maxspeed = 0
    _name = ""
 
    def __init__(self):
        self._maxspeed = 200
        self._name = "Supercar"
 
    def drive(self):
        print 'driving. maxspeed ' + str(self._maxspeed)

    def _drive(self):
        print 'driving. maxspeed ' + str(self._maxspeed)


obj = Car()
print dir(obj)


class Audi(Car):
	pass

audi_obj = Audi()
print dir(audi_obj)

def _private():
	print "Private"

import ipdb;ipdb.set_trace()