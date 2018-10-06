# defining a function called cheese_and_crackers which takes two arguments i.e. it has two parameters and then prints 
# the values of those arguments.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
# Calling/running/using the function and passing numbers as arguments.
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# creating two varibles which will act as arguments for our function.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# Passing the above variables as arguments to the function.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Doing maths inside.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Combining maths and variables to get a list of final arguments.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

