from INTERFACE.directories import *
from INTERFACE.image_generator import *
from player import *

class Player_Deck(Img):

    display_info_player = {1:False, 2:False, 3:False, 4:False, 5:False,
                           6:False, 7:False, 8:False, 9:False}

    def __init__(self, master):
        super().__init__(master)
        self.position_y_default = 380
        self.__card_game_positions()

    def __card_game_positions(self):

        if self.display_info_player[1]:
            self.player_first_card = self.first_card(position_y=300)
        else:
            self.player_first_card = self.first_card()

        if self.display_info_player[2]:
            self.player_second_card = self.second_card(position_y=300)
        else:
            self.player_second_card = self.second_card()


    def __build_image_card(self,card_position_list, position_x, position_y, card_clicked):
        global card_panel
        cards = {1:'self.first_card_clicked', 2:'self.second_card_clicked',
                 3:'self.third_card_clicked', 4:'self.fourth_card_clicked',
                 5:'self.fifth_card_clicked', 6:'self.sixth_card_clicked',
                 7:'self.seventh_card_clicked', 8:'self.eighth_card_clicked',
                 9:'self.nineth_card_clicked'}

        func = eval(cards[card_clicked])

        card_name = player_cards[card_position_list][0] + '_' + player_cards[card_position_list][1] + '.png'
        file_image = file_cards + card_name

        img = self.show_image(file_image)

        card_panel = Button(self.master, image=img, borderwidth=0)
        card_panel.image = img
        card_panel.bind('<Button-1>', func)
        card_panel.place(x=position_x, y=position_y)

    def __destroy_cards(self):
        global card_panel
        print(card_panel)
        card_panel.destroy()


    def first_card(self, position_x=0, position_y=None):

        if position_y == None:
            position_y = self.position_y_default

        self.__build_image_card(0, position_x, position_y, 1) # player[0] = rank_card
                                                 # player[1] = suit_card

    def first_card_clicked(self, event=None):
        if self.display_info_player[1]:
            self.display_info_player[1] = False
        else:
            self.display_info_player[1] = True

        self.__destroy_cards()
        self.__card_game_positions()

    def second_card(self,position_x=90, position_y=None):

        if position_y == None:
            position_y = self.position_y_default

        self.__build_image_card(1,position_x, position_y, 2) # player[1] = rank_card
                                                 # player[1] = suit_card

    def second_card_clicked(self, event=None):
        print('Rafa')