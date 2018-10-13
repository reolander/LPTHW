print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = int(raw_input("> "))

if door == 1:
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == '1':
		print "The bear eats your face off. Good job!"
		print "1. To regenerate the face."
		print "2. To be faceless for the rest of your life but still be breathing."
		
		face = raw_input('> ')
		
		if face == '1':
			print "You got a new face bro!"
		elif face == '2':
			print "You can live but without face!"
		else:
			print "You are fucking dead bro!"
			
	elif bear == '2':
		print "The bear eats your legs off. Good job!"
	else:
		print "Well doing %s is probably better. Bear runs away." % bear
		
elif door == 2:
	print "You state into the endless abyss at the Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == '1' or insanity == '2':
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
		
elif 3 <= door <= 1000:
	print "You stumble around and fall on a kinfe and die. Good job!"

else:
	print "What the fuck did you type in! Follow the bloody instructuions!"