print "How old are you?",
age_years = int(raw_input())
age_days = age_years * 365
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (age_years, height, weight)

print "So you're %d years old (%d days old), %s tall and %s heavy." % (age_years, age_days, height, weight)
