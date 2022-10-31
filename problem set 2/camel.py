char1='a'
print(ord(char1))




#change camelCase to snake_case using ascii syastem
#take an input 
# string = input('yourName : ')
# # to recognize capital letter check if its int value falls under 65-90 in a for loop(oneway)
# #to define make a list that contains all the int values (2nd way)
# number = ['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# for i in string:
#     if i in number :
#         #if capital letter replace it with _small letter
#         string = string.replace(i,'_'+i.lower())
# print('your_name :', string)       

















#change camelCase to snake_case using ascii syastem
#take an input 
string = input('yourName : ')
# to recognize capital letter check if its int value falls under 65-90 in a for loop(oneway)
for i in string:
    if ord(i) in range(65,90):
        #if capital letter replace it with _small letter
        string = string.replace(i,'_'+i.lower())
print('your_name :', string)       
































