from INTERFACE.directories import *
from INTERFACE.image_generator import *
from player import *

func_buttom = [
    'first', 'second', 'third', 'fourth',
    'fifth', 'sixth', 'seventh', 'eighth', 'nineth'
                                                    ]

display_info_player = {
                        x: {'CARD_NUM': x,'UP': False, 'BUTTOM': None,
                            'BUTTOM_FUNC': ''.join('self.' + func_buttom[x-1] + '_card_clicked')}
                                            for x in range(1, 10)
                                                                    }
card_up = 0
potential_changes = []

class Player_Deck(Img):

    def __init__(self, master):
        super().__init__(master)
        self.card_game_positions()

    def card_game_positions(self):
        for number in range(9):
            if display_info_player[number + 1]['UP'] and \
                    display_info_player[number + 1]['CARD_NUM'] == card_up:
                self.build_image_card(card_position_list=number,
                                        position_x=number*90,
                                        position_y=300)

            else:
                self.build_image_card(card_position_list=number,
                                        position_x=number*90,
                                        position_y=380)

    def build_image_card(self, card_position_list,
                           position_x, position_y):

        card_name = player_cards[card_position_list][0] + '_' \
                    + player_cards[card_position_list][1] + '.png'

        file_image = file_cards + card_name

        func = eval(display_info_player[card_position_list + 1]['BUTTOM_FUNC'])

        img = self.show_image(file_image)
        card_panel = Button(self.master, image=img, highlightthickness=0)
        card_panel.image = img
        card_panel.bind('<Button-1>', func)
        card_panel.place(x=position_x, y=position_y)
        display_info_player[card_position_list + 1]['BUTTOM'] = card_panel

    def card_clicked(self, position):
        global card_up
        card_up = position

        if display_info_player[position]['UP']:
            display_info_player[position]['UP'] = False
        else:
            display_info_player[position]['UP'] = True

        destroy_cards()
        self.card_game_positions()

    def first_card_clicked(self, event=None):
        self.card_clicked(1)

    def second_card_clicked(self, event=None):
        self.card_clicked(2)

    def third_card_clicked(self, event=None):
        self.card_clicked(3)

    def fourth_card_clicked(self, event=None):
        self.card_clicked(4)

    def fifth_card_clicked(self, event=None):
        self.card_clicked(5)

    def sixth_card_clicked(self, event=None):
        self.card_clicked(6)

    def seventh_card_clicked(self, event=None):
        self.card_clicked(7)

    def eighth_card_clicked(self, event=None):
        self.card_clicked(8)

    def nineth_card_clicked(self, event=None):
        self.card_clicked(9)

def run(master):
    Player_Deck(master)

def get_card_up():
    for card in display_info_player:
        if display_info_player[card]['UP'] == True:
            return card

def destroy_cards():
    for x in range(1, 10):
        display_info_player[x]['BUTTOM'].destroy()
