# implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and 
# then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains,
#  output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate
#  that the tank is essentially full.

#If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary
#  for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionErro.




def main() :
    fraction=get_percent(input('fraction: '))
    while(fraction=='invalid'):
        fraction = get_percent(input('fraction: '))
    
    if(isinstance(fraction, int)):
        print(fraction,'%',sep='')
    else:
        print(fraction)
    

def get_percent(fraction) :
    x , y = fraction.split('/')
    try :
        if (int((int(x)/int(y)) * 100)) >= 100 :
            return 'F'
        elif (int((int(x)/int(y)) * 100)) <= 0 :
            return 'E'
        else:
            return int((int(x)/int(y)) * 100)
    except ValueError:
            return 'invalid'
    except ZeroDivisionError :
            return 'invalid'
    
           
           
       
        
            
            
        
main()