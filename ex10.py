# _*_ coding: utf-8 _*_

tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat"
verti_cat = "\vI'm vertically tabbed."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies 
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print verti_cat

print "\xAE \o12"

# while True:
#	for i in ["/", "-", "|", "\\", "|"]:
#		print "%s\r" % i,

print "Hello my name is: \t%s" % "lol"
health = "fine"
print "Hello.\n How are you doing. I'm \"%s\"" %health