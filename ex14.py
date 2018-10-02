from sys import argv

script, name, user_name = argv
prompt = '>'

print "Hi %s, I'm the %s script." %(name, script)
print "I'd like to ask you a few questions."
print "Enter the Username that you would like to use %s." % name
user_name = raw_input(prompt)

print "Do you like me %s? " % user_name
likes = raw_input(prompt)

print "Where do you live %s? " % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print '''
Allright %s, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
''' % (user_name, likes, lives, computer)