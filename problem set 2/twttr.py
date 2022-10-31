# implement a program that prompts the user for a str of text and then outputs that same text but with all vowels
#  (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

#ask for input 
text = input('input: ')
#make a list of vowels
# vowels = ['A','E','I','O','U']

#use for loop and identify the charaters 
for i in text :
    if i in ('A','E','I','O','U','a','e','i','o','u'):
        text = text.replace(i,'')
print( 'output:' , text.lower())
   
#replace the char that falls with nothing
#use print state with lower()

