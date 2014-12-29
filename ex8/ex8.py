#Setting the variable formatter to have values of four variables inserted
formatter = "%r %r %r %r"

# prints 1,2,3,4
print formatter % (1, 2, 3, 4)

## Prints one, two, three, four
print formatter % ("one", "two", "three", "four")

## sets boolean values to the variables
print formatter % (True, False, False, True)

### %r will print the raw character so, it prints the raw value of formatter variable 4 times, which is 4*4 strings of %r 
print formatter % (formatter, formatter, formatter, formatter)

### Prints the each of the four strings for each %r
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
