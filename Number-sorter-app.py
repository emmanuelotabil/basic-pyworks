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
    evens = evens.sort()
    odds = odds.sort()
    print(evens)
    print(odds)