#we can combine strins with +
from platform import python_branch


name01 = 'sneha'
name02 = 'hota'
print(name01 + name02)
print('debug','hello',name01,name02)
# modifying a string
say='i am learning python '
print(say.upper())
print(say.lower())
print(say.capitalize())
print(say.count('a'))#it count no. of 'a' in the string``

name1 = input('enter your first name:')
name2 = input('neter your last name:')
print('hello', name1.capitalize(), name2.capitalize())
print('hello', name1.upper(), name2.upper())
print('hello', name1.lower(), name2.lower())
print( name1.count('a') + name2.count('a'))

