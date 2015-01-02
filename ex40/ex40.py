class Song(object):
	def __init__(self, singer, song_name, lyrics):
		self.lyrics = lyrics
		self.song_name = song_name
		self.singer = song_name
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			

lyrics = {'happy_bday':['Happy birthday to you', 'Didn\'t know singing this gets you sued','Might as well stop it right now'], 'bulls_on_parade':['They rally around tha family', 'With pockets full of shells']}


	
			
happy_bday = Song('Unknown', 'Unknown', lyrics['happy_bday'])
happy_bday.sing_me_a_song()

print '-' * 10

bulls_on_parade = Song('Someone','Bulls on a Parade', lyrics['bulls_on_parade'])
bulls_on_parade.sing_me_a_song()


