## import argv from sys module
from sys import argv

## take script name as script and filename as the parameter 
script, filename = argv


## open the file for reading
txt = open(filename)

## Print filename provided
print "Here's your file %r:" % filename

## Reads the file
print txt.read()


## Type again
print "Type the filename again:"

### get input from user manually
file_again = raw_input("> ")


### open the second file for reading
txt_again = open(file_again)


## reads the second file 
print txt_again.read()

## Close both files
txt.close()
txt_again.close()
