import datetime

time = datetime.datetime.now()
month = time.month
day = time.dayhour 
hour = time.hour
minute = time.minute

users = ['James','John','Kate','Celine','Hannah']

print('\t\tHi there! Welcome to the Shipping Account Program')

user_input = input('\n\nEnter your username: ').capitalize()

if user_input in users:
    print('\n\t\tHello ',user_input,',Welcome to your account.')
    print('\n\t\tShipping Prices ')
    print('Shipping orders 0 to 100:            $5.10 each')
    print('Shipping orders 100 to 500:            $5.00 each')
    print('Shipping orders 500 to 1000:            $4.95 each')
    print('Shipping orders over 1000:            $4.80 each')

    num_items = int(input('\nHow many items will you like to ship?: '))

    if num_items <= 100:
        cost = round(5.10*num_items,2)
        print('\nYour total cost is $',cost)

    elif num_items in range(101,500):
        cost = round(num_items*5.00)
        print('Your total cost is $',cost)

    elif num_items in range(501,1000):
        cost = round(4.95*num_items,2)
        print('Your total cost is ',cost)
        
    else:
        cost = round(num_items*4.80)
        print('Your total cost is $',cost)
