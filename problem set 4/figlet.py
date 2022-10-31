#implement a program that:
#Expects zero or two command-line arguments:
#zero if the user would like to output text in a random font.
#Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and
#  the second of the two should be the name of the font.
#Prompts the user for a str of text.
#Outputs that text in the desired font.

import random 
from pyfiglet import Figlet
import sys

text = input ('Input: ')
try:
    figlet = Figlet()
    figlet.getFonts()
    if len(sys.argv) == 1 :
        random_font = random.choice(figlet.getFonts())
        figlet.setFont(font=random_font)
        print(figlet.renderText(text))
    elif len(sys.argv) in range (1,3) and sys.argv[1] == '-f' or '--font' :
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))
except IndexError :
    print ('please give valid command line arguments')
except:
    print('fond not found')







        
         


    
    
