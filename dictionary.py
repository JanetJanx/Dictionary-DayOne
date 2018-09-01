#function to generate the dictionary keys and values
def dictinary(a,b):
    if type(a) == int and type(b) == int:
        #variable for the empty dictionary
        sq_number = dict()
        #create dictionary keys as numbers with values as their squares
        for n in range(a,b):
            sq_number[n] = n**2
        return sq_number
    else:
        return "Please use numbers(integers)"

#print the generated dictinary
print dictinary('r',15)