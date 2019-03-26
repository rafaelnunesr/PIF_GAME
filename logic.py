from collections import defaultdict

cards_values = {'A':1, 'J':11, 'Q':12, 'K':13, '-':0}



from collections import defaultdict

cards = [('1', 'SPADES'), ('2', 'SPADES'),
       ('3', 'DIAMONDS'), ('3', 'SPADES'),
       ('3', 'CLUBS'), ('3', 'HEARTS'),
       ('4', 'CLUBS'),  ('5', 'CLUBS'),
        ('6', 'CLUBS') ]
        
def check_cards(cards_dict):
	
	sequences = defaultdict(lambda: 0)

	sequence_a = False
	sequence_b = False
	sequence_c = False
	
	for sequence in cards_dict.values():
		if len(sequence) > 3:
			for num in sequence:
				if str(num) == sequences[str(num)]:
					sequences[str(num)] += 1
					del sequences[str(num)]
		sequences[str(sequence)] += 1
	
	print(sequences)
	
def categorize_by_rank(card_list):
	
	suits = {'HEARTS':[], 'DIAMONDS':[],
	         'CLUBS':[], 'SPADES':[]}
	
	for card in card_list:
		suits[card[1]].append(card[int(0)])
	
	return suits
	         

b = categorize_by_rank(cards)
check_cards(b)


        

