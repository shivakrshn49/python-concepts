class Slots(object):
    __slots__ = ['x', 'y']

    def __getattr__(self, attr):
        print self, attr



obj = Slots()