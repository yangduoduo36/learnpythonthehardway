## Function with 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"


## Passing numbers directly while passing the function
print "We can just give the function numbers directly."
cheese_and_crackers(20,30)

print "OR we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50


## Passing variables when calling cheese_and_crackers function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


## Perform addition and then passing those values as numbers to the functions.
print "We can even do math inside:"
cheese_and_crackers(10 + 20, 5 + 6)


## Incrementing the values of variables when passing them to the function.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


### Study drill

def custom(arg1):
	print "%r is arg1" % arg1

custom(1)
custom("1")
one = 1
custom(one)
custom(one+1)
custom(1+1)
custom(cheese_and_crackers(10,20))
custom(raw_input("Enter something: "))
