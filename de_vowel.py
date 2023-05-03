vowels = ['a','e','i','o','u','A','E','I','O','U']
string = ''
count_vowels = 0
def check_letter(letter):
    global string_seperated, count_vowels
    for vowel in vowels:
        if letter == vowel:
            string_seperated.remove(letter)
            count_vowels = count_vowels + 1
def de_vowel(string):
    ''''''
    global string_seperated, count_vowels
    string_seperated = []
    no_vowels = ''
    count_vowels = 0
    for letter in string:
        string_seperated.append(letter)
    for letter in string_seperated:
        check_letter(letter)
    for letter in string_seperated:
        no_vowels = no_vowels + str(letter)
    print(no_vowels)
    print(count_vowels)
string = 'abcd'
de_vowel(string)
string = 'this sentence has no vowels'
de_vowel(string)