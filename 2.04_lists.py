#nickelson, ronald
#2/23/23
#intro to cs

prizes = ('car', 'house', 'plane', 'boat', 'supercar', 'mansion', 'jet', 'yacht', 'apple', 'dirt')
number = int(input('pick a door between 1 and 10: '))
if number >= 1 and number <= 10:
    print(prizes[number - 1])
else:
    print('You lost nerd')