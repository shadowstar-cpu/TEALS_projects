#Nickelson, Ronald
#3/6/23
#Intro to CS
import random
def birthday_song(name):
    """ 
    birthday_song prints a personalized birthday song to stdout
    parameter: name, a person's name (string)
    returns: None
    """
    print('Happy birthday to you \nHappy birthday to you \nHappy birthday, dear ' + name + '\nHappy birthday to you')
birthday_song('Ronnie')

numbers = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']

def Poker_hand():
    '''
picks 5 cards using the lists above
first line sets a variable named number_cards to a list containing 5 random indexes of the numbers list picking the number of the 5 cards
second line sets a variable named suit_cards to a list containing 5 random indexes of the suits list picking the suit of the 5 cards
third line sets a variable named chosen_cards to the corressponding index of both the number_cards list and the suit_cards list, with a text of ' of ' in the middle creating a basic phrase, example ace of hearts
fourth line prints the list of cards with a starting text of 'Your cards are' and commas and spaces inbetween each item creating a sentence like Your cards are Ace of hearts, 2 of diamonds, 3 of spades, 4 of clubs, and king of hearts
    '''
    number_cards = [numbers[(random.randint(0, 12))], numbers[(random.randint(0, 12))], numbers[(random.randint(0, 12))], numbers[(random.randint(0, 12))], numbers[(random.randint(0, 12))]]
    suit_cards = [suits[(random.randint(0, 3))], suits[(random.randint(0, 3))], suits[(random.randint(0, 3))], suits[(random.randint(0, 3))], suits[(random.randint(0, 3))]]
    chosen_cards = [(number_cards[0] + ' of ' + suit_cards[0]), (number_cards[1] + ' of ' + suit_cards[1]), (number_cards[2] + ' of ' + suit_cards[2]), (number_cards[3] + ' of ' + suit_cards[3]), (number_cards[4] + ' of ' + suit_cards[4]), ]
    print('Your cards are ' + chosen_cards[0] + ', ' + chosen_cards[1] + ', ' + chosen_cards[2] + ', ' + chosen_cards[3] + ', and ' + chosen_cards[4])
Poker_hand()