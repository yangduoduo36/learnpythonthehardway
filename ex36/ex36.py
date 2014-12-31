def q1():
	choice = raw_input("Door 1: left or right? > ")
	return choice

def game(choice, fought):
	if choice == "left":
		choice = raw_input("You see a giant guarding the door. fight? run? > ")
		if choice == "fight":
			if fought == False:
				fought = True
				print "You fought valiantly and hurt the giant, but blacked out in the effort."
				print "You wake up and find yourself at the initial point"
				game(q1(),fought)
			else:
				print "You win....... a bag of magic sand, although we highly doubt it's magical. Bye bye."
				exit()
		elif choice == "run":
			print "You ran for your life."
			game(q1(), fought)
		else:
			print "You idiot! You died coz you didn't choose to fight or run"
			exit(0)
	elif choice == "right":
		print "You opened the door to another dimension! You are now in a parallel dimension and your alternate personality in another dimension sees you, is scared by you and kills you off!"
		exit(0)
	else:
		print "What the hell were you thinking? Go back and try again doofus!"
		game(q1(), fought)

fought = False		
game(q1(), fought)
