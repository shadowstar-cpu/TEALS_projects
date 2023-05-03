import random
print('your role is: ' + str(random.randint(1, 6)))

import random
deck = 'ace two three four five six seven eight nine ten jack queen king'.split()
suit = 'spades clubs hearts diamonds'.split()
random.shuffle(deck)
random.shuffle(suit)
print('your card is the ' + deck[1] + ' of ' + suit[1] + '. ')\


responses = ['It is certain','Reply hazy, try again',"Don't count on it",'It is decidedly so'
,'Ask again later','My reply is no','Without a doubt','Better not tell you now'
,'My sources say no','Yes definitely','Cannot predict now','Outlook not so good'
,'You may rely on it','Concentrate and ask again','Very doubtful','As I see it, yes'
,'Most likely','Outlook good','Yes','Signs point to yes']

question = input('Please ask a yes or no question and the mnagic 8 ball will answer you. ')
print('the magic 8 ball says ' + responses[random.randint(0,19)])