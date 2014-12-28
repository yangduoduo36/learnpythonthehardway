my_name = 'Nitin Venkatesh'
my_age = 25 
my_height_inches = 74
my_height_cms = my_height_inches * 2.54
my_height_feet = my_height_cms / 30.48
my_weight_pounds = 180
my_weight_kgs = my_weight_pounds / 2.20
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall, which is %.2f in cms and %.2f in feet" % (my_height_inches, my_height_cms, my_height_feet)
print "He's %d pounds heavy which is %d in kilos" % (my_weight_pounds, my_weight_kgs)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height_inches, my_weight_pounds, my_age + my_height_inches + my_weight_pounds)

## From the python documentation
print "Hickory dickory %(dock)s, the mouse went around the %(clock)s at %(time)02d 'O clock." %{"dock":"dock", "clock":"clock", "time":7}

### Raw print
print "%r" % my_height_feet