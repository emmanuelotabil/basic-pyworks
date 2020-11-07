#Welcome the user
print('\t\tWelcome to the Database Admin Program.')

#Create empty dictionary containing unsernames and passwords
log_on_information = {'admin00':'pass0000','admin01':'pass0001','admin02':'pass0002','admin03':'pass0003','admin04':'pass0004'}

user_name = input('Enter your username: ')

#Validate username
if user_name in log_on_information.keys():

    i = list(log_on_information.keys()).index(user_name)

    password = list(log_on_information.values())[i]

    passkey = input('Enter your password: ')

#Validate password
    if passkey == password:
        print('You are logged in!!')

    else:
        print('Password is incorrect. Please provide a right entry.')

else:
    print('Username not found. Please enter a correct username.')