class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line 
		print "\nThank you for listening\n" 	
			
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

# hello = Song("What the fuck is this?!")

summer_lyrics = ["I got my first real six string",
			     "Bought it at the five and dime",
				 "Played it till my fingers bled"]
				 
summer_of_sixety = Song(summer_lyrics)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

summer_of_sixety.sing_me_a_song()

# hello.sing_me_a_song()