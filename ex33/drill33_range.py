def top_bottom(n,inc):
	i = 0
	numbers = []
	
	for i in range(0,n):
		numbers.append(i)
		i += inc
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers:" 
		
	for num in numbers:
		print num,

ans = input("What number dude? > ")
inc = input("Increment by? > ")
top_bottom(ans,inc)
