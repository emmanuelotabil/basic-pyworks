print('\t\tWelcome to the Number Sorter App!')

running = True

#Run program with while loop
while running:

    #Get user input for comma separated values
    numbers_string = input('\nEnter a series of comma separated numbers(,): ')

    numbers_string = numbers_string.replace(' ','')

    #convert string to list    
    numbers_list = numbers_string.split(',')
    
    #initialize list of even/odd numbers
    evens = []
    
    odds = []
    
    #Calculate for even/odd number
    for n in numbers_list:
    
        n = int(n)
    
        if n % 2 == 0:
    
            evens.append(n)
            print('\n\t\t-Result/Outcome')
            print('\n-'+str(n)+ ' is even')
    
        else:
            odds.append(n)
            print('\n-'+str(n)+ ' is odd')
    
    #Sort list of evens and odds
    evens.sort()
    
    odds.sort()

    #Display even numbers
    print('Below are the even numbers')
    for i in evens:
        print('\n-',i)

    #Display odd numbers
    print('Below are the odd numbers')
    for x in odds:
        print('\n-',x)
    
    #Determine if user will continue or not
    user_continue = input('\nWill you like to continue(y or n): ').lower()
    
    if user_continue != 'y':
        running = False
    
        print('\nThank you for using the program.')