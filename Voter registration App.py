print('Welcome to the Voter Registration App')
user_name = input('Enter your nme??')
user_age =  input('How old are you?: ')
parties = ['Republican','Democratic','Independent','Libertarian','Green']
if user_age>= 18:
    print('Congratulations ',user_name, ', you are eligible to vote.')
    for p in parties:
        print()