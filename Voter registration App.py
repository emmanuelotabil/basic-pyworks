print('\t\tWelcome to the Voter Registration App')
print('\t\t\nThis is a program that will simulate registering to vote.')

user_name = input('\nEnter your name?: ').capitalize()

user_age =  int(input('\nHey '+user_name+', How old are you?: '))

parties = ['Republican','Democratic','Independent','Libertarian','Green']

if user_age>= 18:

    print('\nCongratulations ',user_name, ', you are eligible to vote.')
    
    print('\nThe list of available parties is showm below: ')
    
    for p in parties:
    
        print('-',p)
    
    user_party = input('\nWhat party will you like to join?: ').capitalize()

    if user_party in parties:
    
        print('\nKudos ',user_name,', you have joined the ',user_party, ' party')

        if user_party =='Republican' or 'Democratic':

            print('\nYour selected party is a major party.')

        elif user_party == 'Independent':

            print('\nYou are an independent person.')

        else:

            print('\nYour party is not a major party.')

    else:

        print('\nYour chosen party is not listed.')

else:

    print('\nYou are not eligible to vote')