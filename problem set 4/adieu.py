#implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input 
# at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and 
# n names with n-1 commas and one and, as in the below:
import inflect 
name = []
while True :
    try:
        name_ = input ('Name: ')
        name.append(name_)

    except KeyboardInterrupt :
        print()
        p = inflect.engine()
        name = p.join(name,final_sep="")
        print ('Adieu, adieu, to',name)
        break