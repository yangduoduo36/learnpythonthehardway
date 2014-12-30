from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C"
print "If you do want that, hit RETURN."
raw_input("?")

## Open file in write mode
print "Opening the file..."
target = open(filename, 'w')

### Empty contents of file
print "Truncating the file. Goodbye!"
target.truncate()

### 3 lines of content
print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

### Write 3 lines to the file
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

## Study drill - compress above target.write into 1

target.write("%s\n%s\n%s\n" % (line1,line2,line3))

## Closing the file
print "And finally we close it."
target.close()


