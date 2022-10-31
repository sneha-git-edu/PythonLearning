#mplement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8,
#  1636, wherein the month in the latter might be any of the values in the list below:
#Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again.
#  Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
def main() :
    date = input('Date: ')
    while 'invalid':
        date = (input('Date: '))
        date = date.capitalize()
        print (standard(date))
        
def standard(date) :
    months = {
        "January": '01',
        "February":'02',
        "March":'03',
        "April":'04',
        "May":'05',
        "June":'06',
        "July":'07',
        "August":'08',
        "September":'09',
        "October":'10',
        "November":'11',
        "December":'12'
    }
    try:
        date = date.replace('/', ' ')
        x,y,z = date.split(' ')
        if x in months.keys():
            return z +'-' + months.get(x) + '-' + y
        else:
            return z +'-' + x + '-' + y
    except ValueError :
        return 'invalid'
    
        
        
        


        

         
    
main()






