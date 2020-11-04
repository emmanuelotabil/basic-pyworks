import datetime

time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

food_items = ['Meat','Cheese']

print('\t\tHey there! Welcome to the Grocery List App')

print('\n\nYour current date and time is ',time)

print('\nThe items in your grocery are ',food_items)

item = input('\nEnter the name of a food item: ').capitalize()
food_items.append(item)
item = input('\nEnter another food item: ').capitalize()
food_items.append(item)
item = input('\nEnter a last food item": ').capitalize()
food_items.append(item)
print('\nYour food items are :',food_items)
food_items.sort()

print('\nYour grocery items in alphebetical order is :',food_items)

print('\t\tSimulating Grocery Shopping')


print('\nYour current grocery has ',len(food_items),' items')

print(food_items)
item_1 = input('What food item did you just buy?: ').capitalize()
food_items.remove(item_1)

print(item_1,' has been removed from the grocery list.')

print('\nCurrent grocery has ',len(food_items),' items.')
print(food_items)

item_2 = input('What food item did you just buy?: ').capitalize()
food_items.remove(item_2)

print(item_2,' has been removed from your grocery list.')