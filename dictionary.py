#variable for the empty dictionary
sq_number = dict()

#function to generate the dictionary keys and values
def dictinary():
    #create dictionary keys as numbers with values as their squares
    for n in range(1,16):
        sq_number[n] = n**2
    return sq_number

#print the generated dictinary
print dictinary()