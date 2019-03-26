from deck_cards import french_cards_shuffled as deck

player_cards = []
cpu_cards = []


def give_initial_cards():

    '''It takes the first 18 cards from french_cards_shuffled,
    and it gives 9 cards for player and cpu'''

    for i in range(18):
        if i % 2 == 0:
            player_cards.append(deck.pop(i))
        else:
            cpu_cards.append(deck.pop(i))


def pick_next_card_from_deck():
    if len(deck) > 0:
        next_card = deck.pop(0)
        return next_card
    return None

def throw_card_from_deck():
    pass

def pick_discarted_card():
    pass


give_initial_cards()