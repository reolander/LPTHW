people = 40
cars = 40
buses = 500

# if cars > people execute the block of code below it else if cars < people execute the code block below it else execute
# the block below else statement.
if cars > people:
	print "We should take the cars."
elif cars < people:	
	print "We should not take cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:	
	print "We can't decide"

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."