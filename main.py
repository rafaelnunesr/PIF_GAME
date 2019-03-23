from deck_cards import french_cards_shuffled as deck

player = []
cpu = []

for i in range(18):
    if i % 2 == 0:
        player.append(deck.pop(i))
    else:
        cpu.append(deck.pop(i))


colors = {'HEARTS':'\033[31m', 'SPARES':'\033[32m',
          'CLUBS':'\033[34m', 'DIAMONDS':'\033[33m', 'JOKER':'\033[37m'}


def sort_cards():

    suits = 'HEARTS SPARES CLUBS DIAMONDS JOKER'


def show_player_cards():
    for card in player:
        rank = card[0]
        suit = card[1]

        print('{} {} {} {}'.format(colors[suit], rank, suit, '\033[0m'))

def show_cpu_cards():
    for card in cpu:
        rank = card[0]
        suit = card[1]

        print('{} {} {} {}'.format(colors[suit], rank, suit, '\033[0m'))
