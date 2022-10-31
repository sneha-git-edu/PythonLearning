country = input ('which country do you live in :')
ask = input ('do you want to know some of popular cuisins of india ??')
if country.lower()== 'india' :
    
    if country.lower() != 'india':
        ask = input('do you want to know some of popular cuisins of india ??')
if  ask.lower() == 'yes' :
    state = input('enter any state neme and get to know their popular cuisine : ')
    if state == 'odisha': 
            cuisine = 'pakhal, local pancakes(pitha), saag, dalma, etc'
            print('some of the popular cuisine are:'+ cuisine)

    elif state == 'punjab':
            cuisine = 'chole and kulche , makke di roti snd sarso da saag, lassi,ghee paratha'
            print('some of the popular cuisine are:'+ cuisine)

    elif state == 'west bengal':
            cuisine = 'Keemar Doi Bora , Kathi Rolls ,Jhal Muri, Daab Chingri ,Shukto ,Bhetki Macher Paturi ,Kosha Mangsho'
            print('some of the popular cuisine are:'+ cuisine)
     
    elif state in 'hydrabad ' 'andra pradesh'  'tamil nadu' :
            cuisine = 'idli , dosa, sambar , cutney , rasam '
            print('some of the popular cuisine are:'+ cuisine)
if ask.lower() == 'no':
     print('okay, sorry we only have indian cuisine list here')

# else : 
# print('sorry we only have indian cuisine list here !!')     