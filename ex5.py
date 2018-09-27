name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'Yellow'
hair = 'Brown'

inch_to_centimeter = 2.54
pound_to_kilo = 0.45

print "Let's talk about %r." % name
print "He's %d inches tall." % height
print "He's %d pounds heavey." % weight
print "Acutally that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is trciky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "Weight in kilo %d and height in centimeters %d." %(weight * pound_to_kilo, height * inch_to_centimeter)