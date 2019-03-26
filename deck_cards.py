from random import randint

suits = 'HEARTS SPADES CLUBS DIAMONDS'.split()

ranks = ['A', '2', '3', '4', '5', '6',
         '7', '8', '9', '10', 'K', 'Q', 'J']

french_cards = [(rank, suit) for suit in suits
                             for rank in ranks
                        ] # deck cards organized

for _ in range(2):
    french_cards.append(('-', 'JOKER')) # Add 2 Jokers to deck of cards


french_cards_shuffled = []

def shuffle_frech_cards():
    while len(french_cards) > 0:

        select = randint(0, len(french_cards)-1)

        french_cards_shuffled.append(french_cards[select])

        french_cards.pop(select)

shuffle_frech_cards()
