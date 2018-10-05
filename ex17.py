from sys import argv ; from os.path import exists ;  script, from_file, to_file = argv  
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two lines on one line too, how?
# in_file = open(from_file)
# indata = in_file.read()

# indata = open(from_file).read()

# print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

open(to_file, 'w').write(open(from_file).read()) # made the logic in just one line. 
print "Allright, all done."

# There is no need to use in_file.close() if you just use indata = open(from_file).read() this command automatically closes the file.
# out_file.close()
# in_file.close()