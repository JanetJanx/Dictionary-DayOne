#function to generate the dictionary keys and values
def dictinary(a,b):
    if type(a) == int and type(b) == int:
        #using the concept of comprehension
        #lets create a dictionary with keys as numbers with values as their squares
        sq_number = {n:n**2 for n in range(a,b)}
        return sq_number
    else:
        return "Please use numbers(integers)"

#print the generated dictinary
print dictinary(4,15)