#Print Welcome message
print('\t\tWelcome to the Voter Registration App')
print('\t\t\nThis is a program that will simulate registering to vote.')

#Get user input for name and age
user_name = input('\nEnter your name?: ').capitalize()

user_age =  int(input('\nHey '+user_name+', How old are you?: '))

#Define list of parties
parties = ['Republican','Democratic','Independent','Libertarian','Green']

#First major condition
if user_age>= 18:

    print('\nCongratulations ',user_name, ', you are eligible to vote.')
    
    print('\nThe list of available parties is showm below: ')
    
    for p in parties:
    
        print('-',p)

#Get user input for party they wish to join    
    user_party = input('\nWhat party will you like to join?: ').capitalize()

    if user_party in parties:
    
        print('\nKudos ',user_name,', you have joined the ',user_party, ' party')

#Print message for party chosen
        if user_party =='Republican':
            print('\nYour selected party is a major party.')

        elif user_party =='Democratic':
            print('\nYour selected party is a major party.')

        elif user_party == 'Independent':

            print('\nYou are an independent person.')

        else:

            print('\nYour party is not a major party.')

    else:

        print('\nYour chosen party is not listed.')

else:
    print('Sorry'+user_name+', you are not eligible to vote.')