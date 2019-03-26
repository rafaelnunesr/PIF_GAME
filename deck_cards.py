from random import shuffle

suits = 'HEARTS SPADES CLUBS DIAMONDS'.split()

ranks = ['A', '2', '3', '4', '5', '6',
         '7', '8', '9', '10', 'K', 'Q', 'J']

french_deck = [(rank, suit) for suit in suits
                             for rank in ranks
                        ] # deck cards organized

for _ in range(2):
    french_deck.append(('-', 'JOKER')) # Add 2 Jokers to deck
    
def shuffle_french_deck():
	shuffle(french_deck)

shuffle_french_deck()
print(french_deck)
