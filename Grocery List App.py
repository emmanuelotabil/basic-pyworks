import datetime

#Creating datetime object
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

#Initial Items in grocery
food_items = ['Meat','Cheese']

#Welcome message
print('\t\tHey there! Welcome to the Grocery List App')

print('\n\nYour current date and time is ',time)

print('\nThe items in your grocery are ',food_items)

#Obtaining user inputs
item = input('\nEnter the name of a food item: ').capitalize()
food_items.append(item)
item = input('\nEnter another food item: ').capitalize()
food_items.append(item)
item = input('\nEnter a last food item": ').capitalize()
food_items.append(item)

#printing and sorting list items
print('\nYour food items are :',food_items)
food_items.sort()

print('\nYour grocery items in alphebetical order is :',food_items)

#simulating Grocery Shopping
print('\t\tSimulating Grocery Shopping')


print('\nYour current grocery has ',len(food_items),' items')

print(food_items)

#Removing first item
item_1 = input('What food item did you just buy?: ').capitalize()
food_items.remove(item_1)

print(item_1,' has been removed from the grocery list.')

print('\nCurrent grocery has ',len(food_items),' items.')
print(food_items)

#Removing second item
item_2 = input('What food item did you just buy?: ').capitalize()
food_items.remove(item_2)

print(item_2,' has been removed from your grocery list.')

print('\nCurrent grocery has ',len(food_items),' items.')
print(food_items)

#Removing third item
item_3 = input('What food item did you just buy?: ').capitalize()
food_items.remove(item_3)

#Out of items
print('\nThe grocery has ',len(food_items),' items now. ')
print(food_items)
no_item = food_items.pop()

print('\n\nYour grocery is out of ',no_item,'.')
new_item = input('What item will you like instead?: ').capitalize()
food_items.append(new_item)

print('\nHere is what you have left on your grocery list: ')
print(food_items)