example_paragraph = 'It was a beautiful day in New York City. Our hero Ariana Grande was on a walk from the Standard to Duane Reade. Ariana Grande was walking rather quickly beacuse she had lived in New York for a few months. All of a sudden a slimy donut appeaered out of nowhere. Ariana Grande decided to prance foolishly instead of dealing with the situation. Thrown off from Duane Reade Ariana Grande decides to go to Times Square instead. What a beautiful day in New York.'
#make all letters lowercase
example_paragraph_lower = example_paragraph.lower()
#remove all periods
example_paragraph_lower_no_punctuation = example_paragraph_lower.replace(".", "")
#convert paragraph into a list of individual strings
example_word_list = example_paragraph_lower_no_punctuation.split(" ")

words_in_paragraph = {}

for word in example_word_list:
    if word not in words_in_paragraph:
        words_in_paragraph[word] = 1
    elif word in words_in_paragraph:
        words_in_paragraph[word] += 1

answer = input('what word do you want to know the frequency of? ')

if answer in words_in_paragraph:
    print(answer + ' appears ' + str(words_in_paragraph.get(answer)) + ' times.')
else:
    print(answer + ' does not appear.')
print(words_in_paragraph)