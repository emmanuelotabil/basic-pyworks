import random

print('Welcome to the Word Guess App')
game_dict = {'sports':['soccer','basketball','baseball','tennis','swimming','hockey'],'continents':['africa','europe','asia','north america','south america','australia'],'colors':['red','blue','green','yellow','white','black'],'fruits':['apple','orange','mango','pear','strawberry','grapes']}
game_keys = []
for key in game_dict.keys():
    game_keys.append(key)
game_values = []
for value in game_dict.values():
    game_values.append(value)
    
running = True
while running:
    i = random.randint(0,len(game_keys)-1)
    game_category = game_keys[i]
