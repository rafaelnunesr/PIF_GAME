from random import randint

suits = 'HEARTS SPARES CLUBS DIAMONDS'.split()

ranks = ['A', '2', '3', '4', '5', '6',
         '7', '8', '9', '10', 'K', 'Q', 'J']

french_cards = [(rank, suit) for suit in suits
                             for rank in ranks
                        ]

for _ in range(2):
    french_cards.append(('-', 'JOKER')) # Add 2 Jokers to deck of cards


french_cards_shuffled = []


while len(french_cards) > 0:

    select = randint(0, len(french_cards)-1)

    french_cards_shuffled.append(french_cards[select])

    french_cards.pop(select)


