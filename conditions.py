# from datetime import datetime
# # today = datetime.now().date().month().year()
# # print(today)
# birthday = input('when is your birthday  (dd/mm/yyyy)?')
# birthday = datetime.strptime( birthday,"%yyyy-%mm-%dd")
# if today == birthday:
#     print ('hey there, happy birthday')
# else:
#      print("can't wait to wish you") 
from datetime import datetime
current_date = datetime.now()
today = str(current_date.day)+'/'+ str(current_date.month) 
birthday = input('when is your birthday  (dd/mm/yyyy)?')
birthday = datetime.strptime( birthday,'%d/%m/%y')
bday= str(birthday.day)+'/'+str(birthday.month)
if today == bday:
    print ('hey there, happy birthday')
else:
     print("can't wait to wish you")


