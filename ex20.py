# Importing the sys package/module and getting argv feature from that package.
from sys import argv

# unpacking the argument variable, the two variables on the left indicate that there should be 2 command line arguments.
script, input_file = argv

# defining a function print_all to print the contents of the file using read() method of files.
def print_all(f):
	print f.read()

# defining a function rewind so that we go back to the first character in the file! 
def rewind(f):
	f.seek(0)

# defining a function called print_a_line so that we print a line each of the file with associated line numbers.
def print_a_line(line_count, f):
	print line_count, f.readline(), # Having a comma next to print will not return \n a new line.
	
# opening the file with name contained in input_file variable.
current_file = open(input_file)

print "First let's print the whole file: \n"

# calling the function print_all to print the contents of the file.
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# calling the function rewind - I don't really understand what this does, maybe it takes me back to character 1 of the file.
rewind(current_file)

print "Now let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1 
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)