words_in_paragraph = {}

def example_to_word_list():
    global example_paragraph, example_paragraph_lower, example_paragraph_lower_no_punctuation, example_word_list
    example_paragraph = 'It was a beautiful day in New York City. Our hero Ariana Grande was on a walk from the Standard to Duane Reade. Ariana Grande was walking rather quickly beacuse she had lived in New York for a few months. All of a sudden a slimy donut appeaered out of nowhere. Ariana Grande decided to prance foolishly instead of dealing with the situation. Thrown off from Duane Reade Ariana Grande decides to go to Times Square instead. What a beautiful day in New York.'
    #make all letters lowercase
    example_paragraph_lower = example_paragraph.lower()
    #remove all periods
    example_paragraph_lower_no_punctuation = example_paragraph_lower.replace(".", "")
    #convert paragraph into a list of individual strings
    example_word_list = example_paragraph_lower_no_punctuation.split(" ")

def dicitionary_of_words():
    global example_word_list
    for word in example_word_list:
        if word not in words_in_paragraph:
            words_in_paragraph[word] = 1
        elif word in words_in_paragraph:
            words_in_paragraph[word] += 1

def max_valued_key(dictionary):
    global max_value, max_value_key, highest_value_list
    max_value = 0
    max_value_key = ''
    for key, value in dictionary.items():
        if dictionary[key] > max_value:
            max_value = dictionary[key]
            max_value_key = key
    del dictionary[max_value_key]
    highest_value_list = [max_value_key, max_value]
    return(highest_value_list)
example_to_word_list()
dicitionary_of_words()
i = 1
while i <= 5:
    print(max_valued_key(words_in_paragraph))
    i+=1