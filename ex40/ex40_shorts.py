mystuff = {'apples':'I am APPLES!'}
print mystuff['apple']

class MyStuff(object):
	def __init__(self):
		self.tangerine = "And now a thousand years between"
	
	def apple(self):
		print "I am a classy apple."
		
thing = MyStuff()
thing.apple()
print thing.tangerine
