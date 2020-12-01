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

    n = random.randint(0,len(game_values)-1)
    game_word = game_dict[game_category][n]

    blank_word = []
    for letter in game_word:
        blank_word.append('- ')

    print('You are to pick a ',len(blank_word),'letter word from the ',game_category,' category')

    guess = ''
    guess_count = 0
    while guess != game_word:
        print(blank_word.join())
        user_input = input('Enter your guess: ')
        guess_count+=1

        if guess == game_word:
            print('Congratulations! You won the game in ',guess_count,' tries')
            break
        else:
            print('Your guess is incorrect. I will reveal one of the words at random.')
            