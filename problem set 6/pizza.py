#implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format,
#  and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table 
# using the library’s grid format. If the user does not specify exactly one command-line argument, or if the specified file’s name
#  does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.
from tabulate import tabulate
import csv
import sys
try:
    file_name = sys.argv[1]

    if len(sys.argv)>2 :
        print('Too many command-line arguments')
        exit()
    if len(sys.argv)>2:
        print('Too few command-line arguments')
        exit()
    if file_name.endswith('.csv') == False:
        print('Not a CSV file')
        exit()
except IndexError :
    print ('Too few command-line arguments')

with open(sys.argv[1],"r") as file:
    print('made it')
    table = csv.DictReader(file)
    if sys.argv[1] =='regular.csv' :
        for row in table :
            print(tabulate(row,headers = "firstrow",tablefmt ="outline"))
    elif sys.argv[1] =='Sicilian.csv' :
        for row in table :
            print(row['Sicilian Pizza'],row['Small'],row['Large'])
    



    # table = tabulate(sys.argv[1], headers = "firstrow",tablefmt ="outline")
    # print(table)
        


