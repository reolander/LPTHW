'''
class Parent(object):
	
	def altered(self):
		print "PARENT altered()"
		
class Child(Parent):
	
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"
	
dad = Parent()
son = Child()

dad.altered()
son.altered()
'''

from ex44_module import Other

class Child():
	
	def __init__(self):
		self.other = Other()
		
	def implicit(self):
		self.other.implicit()
	
	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"
		
son = Child()

son.implicit()
son.override()
son.altered()