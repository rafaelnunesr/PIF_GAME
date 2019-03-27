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
        self.dict_list_cards = {}
        self.sequence_A = []
        self.sequence_B = []
        self.sequence_C = []
        self.extra_cards = []

    def convert_rank_cards(self):

        temp_list_cards = []

        for card in self.list_cards:
            rank, suits = card

            if rank in self.cards_values:
                rank = self.cards_values[rank]

            temp_list_cards.append((int(rank), suits))

        self.list_cards = temp_list_cards

    def categorize_by_suit(self):

        dict_cards = {
            'CLUBS': [], 'DIAMONDS': [],
            'HEARTS': [], 'SPADES': [],
            'JOKER': [] }

        for card in self.list_cards:
            dict_cards[card[1]].append(card[0])

        self.dict_list_cards = dict_cards




run_logic = Logic(player_cards)
run_logic.convert_rank_cards()
run_logic.categorize_by_suit()

