pquit = False
while pquit == False:
    my_dictionary = {
        'idk' : 'I dont know',
        'ttyl' : 'Talk to you later',
        'ty' : 'thank you',
        'wwrrd' : 'what would ryan reynolds do'}
    word = input(' What abbrevation would you like to know.')
    if word == 'quit':
        quit()
    print(my_dictionary.get(word, 'Sorry that isnt in my dictionary.'))