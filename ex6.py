# A variable x with an integer format sequence embedded in a string
x = "There are %d type of people." %10

# A string variable i.e. a variable holding a string
binary = "binary"

# A string variable
do_not = "don't"

# A string variable with other variables embedded in the string
y = "Those we know %s and those who %s." %(binary, do_not)

print x # print x
print y # print y 

print "I said: %r." %x   # Replace %r with value of x including the quotes.
print "I also said: '%s'." %y    # Replace %s with a value of y.

hilarious = False # A boolean variable
joke_evaluation = "Isn't that joke so funny?! %r" # A string variable with a format character

print joke_evaluation %hilarious #print value of joke_evaluation variable by replace the format character with hilarious variable's value.

w = "This is the left side of..."
e = "a string with a right side."

print w + e # concatanation of w and e variables happened. That is these two strings are attached.
