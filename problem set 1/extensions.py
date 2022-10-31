#  implement a program that prompts the user for the name of a file and then outputs that file’s media type if the 
#  file’s name ends, case-insensitively, in any of these suffixes:

# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip
# If the file’s name ends with some other suffix or has no suffix at all, output
#  application/octet-stream instead, which is a common default.



#ask user for file name
file_name = input('File name:')
#lowercase it all foe=r case insesitivity
file_name = file_name.lower()
#check if it contains the character '.'
if file_name.find('.')!= -1 :
#then check the index of '.'
    index = file_name.index('.')
#take the range of character form 0 to '.' to get the desired set of characters from string
    char = file_name[0:index+1]
# then replace teh file name and '.' by image/ like if fle name is cat.gif output it as image/gif
    file_name = file_name.replace(char , 'image/')
    print(file_name)
else :
    print ('application/octet-stream')


    

