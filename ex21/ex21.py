def add(a,b):
	print "adding %d + %d" % (a,b)
	return a+b

def subtract(a,b):
	print "subtracting %d - %d" % (a,b)
	return a-b

def multiply(a,b):
	print "multiplying %d * %d" % (a,b)
	return a*b
	
def divide(a,b):
	print "dividing %d / %d" % (a,b)
	return a/b

print "Let's do some math with just functions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, height: %d, weight: %d, IQ: %d" % (age,height,weight,iq)

# Puzzle for the extra credit

print "Here is a puzzle."

## (age+(height-(weight*(iq/2))))
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

def answer():
	return 42
	
print "What is the secret of life itself? ", answer()


