x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

## Printing line 1 and 2
print x
print y

## Prints line 1 and 2 with substitutions (x and y)
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

## Print line 3
## Prints the joke_evaluation variable and substitutes the hilarious variable for %r
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

## Print line 4
## Adds the w and e strings (concatenates) since they are of the same type
print w + e