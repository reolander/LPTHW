def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a + b
	
def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b
	
def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a,b)
	return a * b

def divide(a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a / b

print "Let's do some maths with just functions!"

age = add(20, 3)
height = subtract(70, 3)
weight = multiply(28, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = divide(age, multiply(height, subtract(weight, add(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# Creating a programming formula for (a+b)^2 = a^2 + b^2 + 2*a*b
print "Let's computer (a+b)^2"

a = int(raw_input("Please input value for 'a': "))
b = int(raw_input("Please input value for 'b': "))

a_plus_b_squared = add(multiply(a,a), add(multiply(b,b), add(multiply(a,b), multiply(a,b))))

print "(a+b)^2: ", a_plus_b_squared

"""
This is a comment? Yep, just tested it, this is how you write multi-line
comments in python!
"""