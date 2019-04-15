from main import player_cards, deck

def change_order_cards(first_card_selected, second_card_position):

    x = first_card_selected
    y = second_card_position

    player_cards[x], player_cards[y] = player_cards[y], player_cards[x]


def exchange_card(card_from_player, card_from_deck):
    original_card = player_cards[card_from_player]
    card_name = original_card[0] + '_' + original_card[1] + '.png'
    player_cards[card_from_player] = card_from_deck
    return card_name





