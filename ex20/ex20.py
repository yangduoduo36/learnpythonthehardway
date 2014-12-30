from sys import argv

### 
script, input_file = argv

## prints the whole file
def print_all(f):
	print f.read()

## get the seeker reading the file back to the beginning
def rewind(f):
	f.seek(0)

## print a particular line 
def print_a_line(line_count, f):
	print line_count, f.readline()
	## Study drill
	print "Value of current_line on this iteration is ", line_count
	
current_file = open(input_file)

print "First let's print the whole file: \n"
print_all(current_file)
print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print these lines:"

current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
