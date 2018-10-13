the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed listts too
# notice we have to use %r since we don't konw what's in items

for i in change:
	print "I got %r" % i
	
# We can also build listst, first start with an empty one
elements = []
# elements = range(0, 100) #we don't need loop to assign values from 0 to 5 to a elements list.

# then use the range function to do 0 to 5 counts
for i in range(0, 50):
	print "Adding %d to the list." % i
	# append is a function that lists understand.
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Element was: %d" % i