from deck_cards import french_cards_shuffled as deck

player_cards = []
cpu_cards = []

for i in range(18):
    if i % 2 == 0:
        player_cards.append(deck.pop(i))
    else:
        cpu_cards.append(deck.pop(i))


colors = {'HEARTS':'\033[31m', 'SPADES':'\033[32m',
          'CLUBS':'\033[34m', 'DIAMONDS':'\033[33m', 'JOKER':'\033[37m'}


def sort_cards():

    suits = 'HEARTS SPARES CLUBS DIAMONDS JOKER'


def show_player_cards():
    for card in player_cards:
        rank = card[0]
        suit = card[1]

        print('{} {} {} {}'.format(colors[suit], rank, suit, '\033[0m'))

def show_cpu_cards():
    for card in cpu_cards:
        rank = card[0]
        suit = card[1]

        print('{} {} {} {}'.format(colors[suit], rank, suit, '\033[0m'))
