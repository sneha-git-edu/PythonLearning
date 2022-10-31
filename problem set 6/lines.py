# implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of
#  lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or 
# if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via 
# sys.exit.
#Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a 
# comment.) Assume that any line that only contains whitespace is blank.
import sys

try:
    file_name = sys.argv[1]

    if len(sys.argv)>2 :
        print('Too many command-line arguments')
        exit()
    if len(sys.argv)>2:
        print('Too few command-line arguments')
        exit()
    if file_name.endswith('.py') == False:
        print('Not a Python file')
        exit()
except IndexError :
    print ('Too few command-line arguments')

try:
    with open(sys.argv[1],"r") as file:
        print('found it')
        count=0
        lines = file.readlines()
    for line in lines:
        if(line != '\n'):
            count=count+1
        if (line.startswith('#')):
            count=count-1
    print(count)
except FileNotFoundError:
    print('File does not exist')

    
    


    


  
    