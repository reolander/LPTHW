# this one is like your scripts with argv
# *args means basically a string or array of strings, you can pass any number of arguments when the parament is *args
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# this takes no arguments
def print_none():
	print "I got nothin'."
	
print_two('Rohan', 'Mohammad')
print_two_again('Rohan', 'Mohammad')
print_one('Naruto')
print_none()