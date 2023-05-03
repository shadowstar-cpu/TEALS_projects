pquit = False
while pquit == False:
    my_dictionary = {
        'idk' : 'I dont know',
        'ttyl' : 'Talk to you later',
        'ty' : 'thank you',
        'wwrrd' : 'what would ryan reynolds do'}
    word = input(' What abbrevation would you like to know.')
    if word in my_dictionary:
        print(my_dictionary.get(word))
    else:
        if word == 'quit':
            quit()
        else:
            print('Sorry that isnt in my dictionary.')