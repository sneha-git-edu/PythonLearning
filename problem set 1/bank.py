# implement a program that prompts the user for a greeting. If the greeting starts with “hello”,
#  output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100.
#  Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

#take input

greeting = input('Greeting:')
greeting = greeting.lower()
# print(greeting)
#find whether greeting is hello 
if greeting.find('hello') != -1 :
    print('$0')
#to check the character in string write string name and index in square bracket
elif greeting[0] == 'h': 
    print ('$20') 
else :
    print ('$100')   



 

#orint output

