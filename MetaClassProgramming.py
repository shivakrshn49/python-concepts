class Class_(object):
    property_ = "Super"

    def function_():
        pass

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

print Class_.__dict__, "<<<<< Class attributes"
object_ = Class_()
# object_.attribute = "Sexy"
print object_.__dict__, "<<<<< Object attributes"
print vars(Class_) == Class_.__dict__
print vars(object_) == {}
print dir(Class_) == dir(object_)
