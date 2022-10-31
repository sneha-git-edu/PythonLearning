#dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), 
# remove the leading $, and return the amount as a float. For instance
# , given $50.00 as input, it should return 50.0.
#percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a 
# decimal digit), remove the trailing %, and return the percentage a
# s a float. For instance, given 15% as input, it should return 0.15.


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = (float( dollars) * float(percent)/100)
    print(f"Leave ${tip:.2f}")

#convert the input into float and remove the dollar sign
def dollars_to_float(d):
     return d.replace("$",'')
     
    

#remove persent sign and divide the input by 100
def percent_to_float(p):
    return p.replace('%','')
   
   
    
    
    
    


main()