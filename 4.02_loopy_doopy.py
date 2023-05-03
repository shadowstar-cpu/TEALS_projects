def fruit_pluralizer(wordlist):
    '''
    changes singular words to plural words
    takes a list of words, changes the words in the list
    '''
    i = 0
    for word in wordlist:
        if word[-1] == 'y':
            wordlist[i] = word[0 : -1] + 'ies'
        else:
            wordlist[i] = word + 's'
        i += 1
word_list = ['apple', 'berry', 'melon']
print('singular words: ' + str(word_list))
fruit_pluralizer(word_list)
print('no longer singular words: ' + str(word_list))
word_list = []
print('singular words: ' + str(word_list))
fruit_pluralizer(word_list)
print('no longer singular words: ' + str(word_list))
word_list = ['apple', 'berry', 'melon', 'pineapple', 'strawberry', 'pie', 'frosting']
print('singular words: ' + str(word_list))
fruit_pluralizer(word_list)
print('no longer singular words: ' + str(word_list))