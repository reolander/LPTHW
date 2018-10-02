# Importing sys module or library for additional features for our script file.
from sys import argv

# Unpacking the argument variable and assigning values in the variables from the left in order.
script, filename = argv

# using the open function to open a file. Methods are functions called on a object or on a variable itself.
txt = open(filename)

# standard printing of output with some formatting.
print "Here's your file %r" % filename

# txt is a variable with a file in it and this file has some commands that it can run on itself. read() command
# reads the content of the file taking no arguments.
print txt.read()
txt.close()

# Standard printing.
print "Type the filename again:"

# Using raw_input function for user input of file name.
file_again = raw_input('> ')
# print open(file_again).read()

# Opening the file and assigning the file object to txt_again varible.
txt_again = open(file_again)

# priting the contents of txt_again file using read() method.
print txt_again.read() 
txt_again.close()