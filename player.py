from main import player_cards, deck

def change_order_cards(first_card_selected, second_card_position):

    x = first_card_selected
    y = second_card_position

    player_cards[x], player_cards[y] = player_cards[y], player_cards[x]


def exchange_card(card_from_deck):

    player_cards[1] = card_from_deck

def accept_card(new_card, old_card):
    pass



