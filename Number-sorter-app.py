print('Welcome to the Number Sorter App!')

running = True

while running:

    numbers_string = input('Enter a series of comma separated numbers: ')

    numbers_string = numbers_string.replace(' ','')
    
    numbers_list = numbers_string.split(',')
    
    evens = []
    
    odds = []
    
    for n in numbers_list:
    
        n = int(n)
    
        if n % 2 == 0:
    
            evens.append(n)
            print(str(n)+ ' is even')
    
        else:
            odds.append(n)
            print(str(n)+ ' is odd')
    
    evens.sort()
    
    odds.sort()
    
    print(evens)
    print(odds)
    
    user_continue = input('Will you like to continue(y or n): ').lower()
    
    if user_continue != 'y':
        running = False
    
        print('Thank you for using the program.')