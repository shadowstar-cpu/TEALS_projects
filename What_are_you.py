#Nickelson, Ronald
#3/5/23
#Intro to CS

#sets list of classes that can be chosen
classlist = ['sage', 'shadow', 'guardian', 'sentinel', 'vanguard', 'commando', 'scoundrel', 'gunslinger', 'sorcerer', 'assassin', 'juggernaut', 'marauder', 'powertech', 'mercenary', 'operative', 'sniper']

#creates list of 16 values 1 for each class
swtorclass = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#prints introduction message
print('Hello! were going to find out what class would be best for you!' + '\nPlease answer each question with "y" for yes and "n" for no.')

#asks the first question and changes the class value based on the answer
user_input = input('Do you like the republic? ')
if user_input == 'y':
    swtorclass[0] = swtorclass[0] + 2
    swtorclass[1] = swtorclass[1] + 2
    swtorclass[2] = swtorclass[2] + 2
    swtorclass[3] = swtorclass[3] + 2
    swtorclass[4] = swtorclass[4] + 2
    swtorclass[5] = swtorclass[5] + 2
    swtorclass[6] = swtorclass[6] + 1
    swtorclass[7] = swtorclass[7] + 1
    swtorclass[8] = swtorclass[8] - 2
    swtorclass[9] = swtorclass[9] - 2
    swtorclass[10] = swtorclass[10] - 2
    swtorclass[11] = swtorclass[11] - 2
    swtorclass[12] = swtorclass[12] - 1
    swtorclass[13] = swtorclass[13] - 1
    swtorclass[14] = swtorclass[14] - 2
    swtorclass[15] = swtorclass[15] - 2

#changes the values in the reverse if the player answers n
else:
    swtorclass[0] = swtorclass[0] - 2
    swtorclass[1] = swtorclass[1] - 2
    swtorclass[2] = swtorclass[2] - 2
    swtorclass[3] = swtorclass[3] - 2
    swtorclass[4] = swtorclass[4] - 2
    swtorclass[5] = swtorclass[5] - 2
    swtorclass[6] = swtorclass[6] - 1
    swtorclass[7] = swtorclass[7] - 1
    swtorclass[8] = swtorclass[8] + 2
    swtorclass[9] = swtorclass[9] + 2
    swtorclass[10] = swtorclass[10] + 2
    swtorclass[11] = swtorclass[11] + 2
    swtorclass[12] = swtorclass[12] + 1
    swtorclass[13] = swtorclass[13] + 1
    swtorclass[14] = swtorclass[14] + 2
    swtorclass[15] = swtorclass[15] + 2
    
#asks the second question and changes the class value based on the answer
user_input = input('Do you want a lightsaber? ')
if user_input == 'y':
    swtorclass[0] = swtorclass[0] + 1
    swtorclass[1] = swtorclass[1] + 1
    swtorclass[2] = swtorclass[2] + 2
    swtorclass[3] = swtorclass[3] + 2
    swtorclass[4] = swtorclass[4] - 1
    swtorclass[5] = swtorclass[5] - 1
    swtorclass[6] = swtorclass[6] - 1
    swtorclass[7] = swtorclass[7] - 1
    swtorclass[8] = swtorclass[8] + 1
    swtorclass[9] = swtorclass[9] + 1
    swtorclass[10] = swtorclass[10] + 2
    swtorclass[11] = swtorclass[11] + 2
    swtorclass[12] = swtorclass[12] - 1
    swtorclass[13] = swtorclass[13] - 1
    swtorclass[14] = swtorclass[14] - 1
    swtorclass[15] = swtorclass[15] - 1

#changes the values in the reverse if the player answers n
else:
    swtorclass[0] = swtorclass[0] - 1
    swtorclass[1] = swtorclass[1] - 1
    swtorclass[2] = swtorclass[2] - 2
    swtorclass[3] = swtorclass[3] - 2
    swtorclass[4] = swtorclass[4] + 1
    swtorclass[5] = swtorclass[5] + 1
    swtorclass[6] = swtorclass[6] + 1
    swtorclass[7] = swtorclass[7] + 1
    swtorclass[8] = swtorclass[8] - 1
    swtorclass[9] = swtorclass[9] - 1
    swtorclass[10] = swtorclass[10] - 2
    swtorclass[11] = swtorclass[11] - 2
    swtorclass[12] = swtorclass[12] + 1
    swtorclass[13] = swtorclass[13] + 1
    swtorclass[14] = swtorclass[14] + 1
    swtorclass[15] = swtorclass[15] + 1

#asks the third question and changes the class value based on the answer
user_input = input('Do you want to use close range? ')
if user_input == 'y':
    swtorclass[0] = swtorclass[0] - 1
    swtorclass[1] = swtorclass[1] + 1
    swtorclass[2] = swtorclass[2] + 2
    swtorclass[3] = swtorclass[3] - 1
    swtorclass[4] = swtorclass[4] + 1
    swtorclass[5] = swtorclass[5] - 1
    swtorclass[6] = swtorclass[6] + 1
    swtorclass[7] = swtorclass[7] - 1
    swtorclass[8] = swtorclass[8] - 1
    swtorclass[9] = swtorclass[9] + 1
    swtorclass[10] = swtorclass[10] + 1
    swtorclass[11] = swtorclass[11] + 2
    swtorclass[12] = swtorclass[12] + 1
    swtorclass[13] = swtorclass[13] - 1
    swtorclass[14] = swtorclass[14] + 1
    swtorclass[15] = swtorclass[15] - 1

#changes the values in the reverse if the player answers n
else:
    swtorclass[0] = swtorclass[0] + 1
    swtorclass[1] = swtorclass[1] - 1
    swtorclass[2] = swtorclass[2] - 2
    swtorclass[3] = swtorclass[3] + 1
    swtorclass[4] = swtorclass[4] - 1
    swtorclass[5] = swtorclass[5] + 1
    swtorclass[6] = swtorclass[6] - 1
    swtorclass[7] = swtorclass[7] + 1
    swtorclass[8] = swtorclass[8] + 1
    swtorclass[9] = swtorclass[9] - 1
    swtorclass[10] = swtorclass[10] - 2
    swtorclass[11] = swtorclass[11] - 2
    swtorclass[12] = swtorclass[12] - 1
    swtorclass[13] = swtorclass[13] + 1
    swtorclass[14] = swtorclass[14] - 1
    swtorclass[15] = swtorclass[15] + 1

#asks the fourth question and changes the class value based on the answer
user_input = input('if you had both would you use the force more than your lightsaber? ')
if user_input == 'y':
    swtorclass[0] = swtorclass[0] + 2
    swtorclass[1] = swtorclass[1] + 1
    swtorclass[2] = swtorclass[2] - 2
    swtorclass[3] = swtorclass[3] - 1
    swtorclass[4] = swtorclass[4]
    swtorclass[5] = swtorclass[5]
    swtorclass[6] = swtorclass[6]
    swtorclass[7] = swtorclass[7]
    swtorclass[8] = swtorclass[8] + 2
    swtorclass[9] = swtorclass[9] + 1
    swtorclass[10] = swtorclass[10] - 1
    swtorclass[11] = swtorclass[11] - 2
    swtorclass[12] = swtorclass[12]
    swtorclass[13] = swtorclass[13]
    swtorclass[14] = swtorclass[14]
    swtorclass[15] = swtorclass[15]

#asks the fifth question and changes the class value based on the answer
user_input = input('would you rather have high health than high damage? ')
if user_input == 'y':
    swtorclass[0] = swtorclass[0]
    swtorclass[1] = swtorclass[1]
    swtorclass[2] = swtorclass[2] + 2
    swtorclass[3] = swtorclass[3] + 1
    swtorclass[4] = swtorclass[4] + 2
    swtorclass[5] = swtorclass[5] + 1
    swtorclass[6] = swtorclass[6]
    swtorclass[7] = swtorclass[7]
    swtorclass[8] = swtorclass[8]
    swtorclass[9] = swtorclass[9]
    swtorclass[10] = swtorclass[10] + 2
    swtorclass[11] = swtorclass[11] + 1
    swtorclass[12] = swtorclass[12] + 1
    swtorclass[13] = swtorclass[13] + 2
    swtorclass[14] = swtorclass[14]
    swtorclass[15] = swtorclass[15]

#changes the values in the reverse if the player answers n
else:
    swtorclass[0] = swtorclass[0]
    swtorclass[1] = swtorclass[1]
    swtorclass[2] = swtorclass[2] - 2
    swtorclass[3] = swtorclass[3] - 1
    swtorclass[4] = swtorclass[4] - 2
    swtorclass[5] = swtorclass[5] - 1
    swtorclass[6] = swtorclass[6]
    swtorclass[7] = swtorclass[7]
    swtorclass[8] = swtorclass[8]
    swtorclass[9] = swtorclass[9]
    swtorclass[10] = swtorclass[10] - 2
    swtorclass[11] = swtorclass[11] - 1
    swtorclass[12] = swtorclass[12] - 1
    swtorclass[13] = swtorclass[13] - 2
    swtorclass[14] = swtorclass[14]
    swtorclass[15] = swtorclass[15]

#asks the sixth question and changes the class value based on the answer
user_input = input('would you rather be fast than have high health? ')
if user_input == 'y':
    swtorclass[0] = swtorclass[0] + 1
    swtorclass[1] = swtorclass[1] + 2
    swtorclass[2] = swtorclass[2]
    swtorclass[3] = swtorclass[3]
    swtorclass[4] = swtorclass[4]
    swtorclass[5] = swtorclass[5]
    swtorclass[6] = swtorclass[6] + 2
    swtorclass[7] = swtorclass[7] + 1
    swtorclass[8] = swtorclass[8] + 1
    swtorclass[9] = swtorclass[9] + 2
    swtorclass[10] = swtorclass[10]
    swtorclass[11] = swtorclass[11] + 1
    swtorclass[12] = swtorclass[12]
    swtorclass[13] = swtorclass[13]
    swtorclass[14] = swtorclass[14] + 2
    swtorclass[15] = swtorclass[15] + 1

#changes the values in the reverse if the player answers n
else:
    swtorclass[0] = swtorclass[0] - 1
    swtorclass[1] = swtorclass[1] - 2
    swtorclass[2] = swtorclass[2]
    swtorclass[3] = swtorclass[3]
    swtorclass[4] = swtorclass[4]
    swtorclass[5] = swtorclass[5]
    swtorclass[6] = swtorclass[6] - 2
    swtorclass[7] = swtorclass[7] - 1
    swtorclass[8] = swtorclass[8] - 1
    swtorclass[9] = swtorclass[9] - 2
    swtorclass[10] = swtorclass[10]
    swtorclass[11] = swtorclass[11] - 1
    swtorclass[12] = swtorclass[12]
    swtorclass[13] = swtorclass[13]
    swtorclass[14] = swtorclass[14] - 2
    swtorclass[15] = swtorclass[15] - 1

#Changes the best_choice variable based on which class has the highest value
best_choice = 0
if swtorclass[best_choice] < swtorclass[0]:
    best_choice = 0
if swtorclass[best_choice] < swtorclass[1]:
    best_choice = 1
if swtorclass[best_choice] < swtorclass[2]:
    best_choice = 2
if swtorclass[best_choice] < swtorclass[3]:
    best_choice = 3
if swtorclass[best_choice] < swtorclass[4]:
    best_choice = 4
if swtorclass[best_choice] < swtorclass[5]:
    best_choice = 5
if swtorclass[best_choice] < swtorclass[6]:
    best_choice = 6
if swtorclass[best_choice] < swtorclass[7]:
    best_choice = 7
if swtorclass[best_choice] < swtorclass[8]:
    best_choice = 8
if swtorclass[best_choice] < swtorclass[9]:
    best_choice = 9
if swtorclass[best_choice] < swtorclass[10]:
    best_choice = 10
if swtorclass[best_choice] < swtorclass[11]:
    best_choice = 11
if swtorclass[best_choice] < swtorclass[12]:
    best_choice = 12
if swtorclass[best_choice] < swtorclass[13]:
    best_choice = 13
if swtorclass[best_choice] < swtorclass[14]:
    best_choice = 14
if swtorclass[best_choice] < swtorclass[15]:
    best_choice = 15

#prints which choice is the players best
print("Your best choice will be " + classlist[best_choice] + ".")