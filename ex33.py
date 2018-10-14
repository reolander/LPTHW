i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	
	print "At the bottim i is %d" % i

print numbers

for number in numbers:
	print number
	
# Using function to create a list. And also take input from the user.

def create_list(number, incrementor):
	list = []
	i = 0
	while i < number:
		list.append(i)
		i += incrementor
	return list

num = int(raw_input("Enter the size of your list: "))
increm = 2
elements = create_list(num, increm)
print elements

def create_list_for_loop(number):
	list = []
	for i in range(0, number):
		list.append(i)
		i += 3 # Can't i use to increment by 2 or 3 i.e. by someother value other than 1?
	return list

num = int(raw_input("Enter the size of your list: "))
elements = create_list_for_loop(num)
print elements