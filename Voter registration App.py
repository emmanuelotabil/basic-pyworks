print('Welcome to the Voter Registration App')

user_name = input('Enter your nme??').capitalize()

user_age =  input('How old are you?: ').capitalize()

parties = ['Republican','Democratic','Independent','Libertarian','Green']

if user_age>= 18:

    print('Congratulations ',user_name, ', you are eligible to vote.')
    
    print('The list of available parties is showm below: ')
    
    for p in parties:
    
        print('-',p)
    
    user_party = input('What party will you like to join?: ').capitalize()
    if user_party in parties:
    
        print('Kudos ',user_name,'! you have joined the ',user_party, ' party')
        print( )