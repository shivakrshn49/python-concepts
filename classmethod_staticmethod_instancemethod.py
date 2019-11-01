class A(object):
	@staticmethod
	def staticmethod():
		print "I am static method"

	@classmethod
	def classmethod(cls):
		print "I am class method", cls, type(cls)

	def instanemethod(self):
		print "I am instnace method", self, type(self)

obj = A()

# object / instance of a class can access all three static, class, instance methods
obj.staticmethod()
obj.classmethod()
obj.instanemethod()

print "*******************************"
# class A can access only classmethod and staticmethod, but not instance method as it takes self
# as first paraments which is an instance iteslf 
A.staticmethod()
A.classmethod()

