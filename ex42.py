## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	
	def legs(self):
		print "I have four legs"

## create a class named Dog that is-a Animal
class Dog(Animal):
		
	## Class Dog has-a function called __init_ that takes self, name as parameters
	def __init__(self,name):
		## Dog has-a name	
		self.name = name

## create a class named Cat which is-a Animal
class Cat(Animal):
	
	## Class Cat has-a function __init__ that takes self, name as parameters.
	def __init__(self, name):
		## Cat has-a name
		self.name = name
		
## Create a class named Person that is-a object
class Person(object):
	## Person has-a function __init__ that takes self, name as parameters
	def __init__(self, name):
		## Person has-a name
		self.name = name
		
		## Person has-a pet
		self.pet = None
		
## Create a class named Employee that is-a Person
class Employee(Person):
	## Employee has-a function __init__ that takes self, name and salary as parameters
	def __init__(self, name, salary):
		## Calling Person's init function to assign name to Employee's name property
		super(Employee, self).__init__(name)
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary
	
## Create a class named Fish that is-a object
class Fish(object):
	pass

## create a class named Salmon that is-a Fish
class Salmon(Fish):
	pass
	
## create a class named Halibut that is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog('Rover')

## satan is-a Cat
satan = Cat('Satan')

## mary is-a Person
mary = Person('Mary')

## mary has-a pet called Satan
mary.pet = satan

## frank is-a Employee
frank = Employee('Frank', 120000)

## frank has-a pet Rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

rover.legs()