#  implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the 
# equivalent number of Joules as an integer.  Assume that the user will input an integer.
#E =mc^2  . E = energy (in joules)
            # m = mass (in kg)
            # c = speed of light (300000000 meters per second)

# ask the use for input of mass in kg
mass = input ('m:')
#multiply the mass with square of c
energy = int(mass)*3**2*10**8
#print the output 
print('E: ' , energy)