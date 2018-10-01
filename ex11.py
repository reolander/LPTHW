print "How old are you?", # prints the said string and the comma at the end makes sure that newline is not addaed.
age = raw_input("--->") # raw_input is an inbuilt python function in v2 that lets user input some values on prompt
						# it can take an argument which is a string to make the prompt more understandable.
print "How tall are you?",
height = raw_input()
print "How much do you weigh",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy" %(age, height, weight) # print the raw data present in height weight and age variables.

age = raw_input("How old are you? ") # Making the above code much more neat by making use of arg of raw_data.
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So you are %r old, %r tall and %r heavy" %(age, height, weight) 

# form 2

name = raw_input("What is your name? ")
country = raw_input("Which country are you from? ")
aspire = raw_input("What do you aspire to become? ")

print "Hello my name is %r, i'm from %r and I aspire to become a %r" %(name, country, aspire)
