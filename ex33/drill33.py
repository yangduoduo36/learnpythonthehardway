def top_bottom(n,j):

	i = 0
	numbers = []

	while i < n:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i += j
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num
		
ans = input("What number dude? > ")
inc = input("Increment by? > ")
top_bottom(ans,inc)
