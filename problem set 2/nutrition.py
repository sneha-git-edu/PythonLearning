# item = input ('item: ')
# item = item.capitalize()
# nutritional_fact = [
#                     {'fruit':'Apple' , 'calories':'130'} ,
#                     {'fruit':'Avocado' , 'calories':'50'} ,
#                     {'fruit':'Banana' , 'calories':'110' },
#                     {'fruit':'Cantaloupe', 'calories':'50' },
#                     {'fruit':'Grapefruit' , 'calories': '60'},                                          
#                     {'fruit':'Grapes' , 'calories':'90' },
#                     {'fruit':'Honeydew Melon', 'calories':'50' },
#                     {'fruit':'Kiwifruit', 'calories':'90' },
#                     {'fruit':'Lemon', 'calories':'15' },
#                     {'fruit':'Lime', 'calories':'20' },
#                     {'fruit':'Nectarine', 'calories':'60' },
#                     {'fruit':'Orange' , 'calories':'80' },
#                     {'fruit':'Peach', 'calories':'60' },
#                     {'fruit':'Pear' , 'calories':'100' },
#                     {'fruit':'Pineapple' , 'calories':'50' },
#                     {'fruit':'Plums' , 'calories':'70' },
#                     {'fruit':'Strawberries' , 'calories':'50' },
#                     {'fruit':'Sweet Cherries' , 'calories':'100' },
#                     {'fruit':'Tangerine' , 'calories':'50' },
#                     {'fruit':'Watermelon', 'calories':'80'}  ]
                   
# for fruits in item :
#     if fruits in nutritional_fact  : 
#         print(fruits)  
#         print(fruits['calories'])
        

fruit = input ('item: ')
fruit = fruit.capitalize()
nutritional_fact = {
					'Avocado':'50' ,
                    'Apple':'130' ,
                    'Cantaloupe':'50' ,
                    'Grapefruit':'60',                                          
                    'Grapes':'90' ,
                    'Banana':'110' ,
                    'Honeydew Melon':'50' ,
                    'Kiwifruit':'90' ,
                    'Lemon':'15' ,
                    'Lime':'20' ,
                    'Nectarine':'60' ,
                    'Orange':'80' ,
                    'Peach':'60' ,
                    'Pear':'100' ,
                    'Pineapple':'50' ,
                    'Plums':'70' ,
                    'Strawberries':'50' ,
                    'Sweet Cherries':'100' ,
                    'Tangerine':'50' ,
                    'Watermelon':'80'
}
                     
if fruit in nutritional_fact.keys():
    print('calories:' , nutritional_fact.get(fruit), sep = '')
    
else:
    exit()









