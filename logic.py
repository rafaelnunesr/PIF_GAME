# from main import *

player_cards = [('J', 'DIAMONDS'), ('2', 'DIAMONDS'),
                ('3', 'DIAMONDS'), ('7', 'HEARTS'),
                ('Q', 'HEARTS'), ('10', 'DIAMONDS'),
                ('A', 'CLUBS'), ('10', 'SPADES'),
                ('K', 'HEARTS')]


class Logic:

    cards_values = {'A': 1, 'J': 11, 'Q': 12, 'K': 13, '-': 0}

    def __init__(self, list_cards):
        self.list_cards = list_cards









run_logic = Logic(player_cards)

