from deck_cards import french_cards_shuffled as deck

player_cards = []
cpu_cards = []

def give_initial_cards():
    for i in range(18):
        if i % 2 == 0:
            player_cards.append(deck.pop(i))
        else:
            cpu_cards.append(deck.pop(i))

give_initial_cards()

