amountdue = 50
while (amountdue > 0)and (amountdue != 0):
    insertcoin = input('insert cois :' )
    if insertcoin in('10','5','25'):
        amountdue = amountdue - int(insertcoin)
    if(amountdue>0):
        print('amount due :' , amountdue)
print('change owed:' , abs(amountdue))








#2 problems 1) when given invalid number it ask for insert coin
#and it prints amount due when amount due reaches o or negative








