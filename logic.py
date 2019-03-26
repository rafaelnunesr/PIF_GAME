from collections import defaultdict

cards_values = {'A':1, 'J':11, 'Q':12, 'K':13, '-':0}



def check_cards(list_cards):

        rank_cards = defaultdict(lambda:0)


        sequence_A = False
        sequence_B = False
        sequence_C = False

        for card in list_cards:

            rank, suit = card

            if rank in cards_values:
                rank = cards_values[rank]

            else:

                rank = int(rank)
            rank_cards[rank] += 1

        print(rank_cards.items())

