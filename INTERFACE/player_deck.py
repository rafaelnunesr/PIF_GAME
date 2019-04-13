from INTERFACE.directories import *
from INTERFACE.image_generator import *
from player import *


class Player_Deck(Img):

    display_info_player = {1:[False, None], 2:[False, None], 3:[False, None],
                           4:[False, None], 5:[False, None], 6:[False, None],
                           7:[False, None], 8:[False, None], 9:[False, None]}


    def __init__(self, master):
        super().__init__(master)
        self.position_y_default = 380
        self.__card_game_positions()

    def __card_game_positions(self):

        if self.display_info_player[1][0]:
            self.first_card(position_y=300)
        else:
            self.first_card()

        if self.display_info_player[2][0]:
            self.second_card(position_y=300)
        else:
            self.second_card()

        if self.display_info_player[3][0]:
            self.third_card(position_y=300)
        else:
            self.third_card()

        if self.display_info_player[4][0]:
            self.fourth_card(position_y=300)
        else:
            self.fourth_card()

        if self.display_info_player[5][0]:
            self.fifth_card(position_y=300)
        else:
            self.fifth_card()

        if self.display_info_player[6][0]:
            self.sixth_card(position_y=300)
        else:
            self.sixth_card()

        if self.display_info_player[7][0]:
            self.seventh_card(position_y=300)
        else:
            self.seventh_card()

        if self.display_info_player[8][0]:
            self.eighth_card(position_y=300)
        else:
            self.eighth_card()

        if self.display_info_player[9][0]:
            self.nineth_card(position_y=300)
        else:
            self.nineth_card()




    def __build_image_card(self, card_position_list, position_x, position_y, card_clicked):

        cards = {1:'self.first_card_clicked', 2:'self.second_card_clicked',
                 3:'self.third_card_clicked', 4:'self.fourth_card_clicked',
                 5:'self.fifth_card_clicked', 6:'self.sixth_card_clicked',
                 7:'self.seventh_card_clicked', 8:'self.eighth_card_clicked',
                 9:'self.nineth_card_clicked'}

        func = eval(cards[card_clicked])

        card_name = player_cards[card_position_list][0] + '_' + player_cards[card_position_list][1] + '.png'
        file_image = file_cards + card_name

        img = self.show_image(file_image)
        card_panel = Button(self.master, image=img, highlightthickness=0)
        card_panel.image = img
        card_panel.bind('<Button-1>', func)
        card_panel.place(x=position_x, y=position_y)
        self.display_info_player[card_position_list + 1][1] = card_panel

    def __destroy_cards(self):
        for x in range(1,10):
            print(self.display_info_player[x][1])
            self.display_info_player[x][1].destroy()

    def __card_clicked(self, position):
        if self.display_info_player[position][0]:
            self.display_info_player[position][0] = False
        else:
            self.display_info_player[position][0] = True

        self.__destroy_cards()
        self.__card_game_positions()

    def first_card(self, position_x=0, position_y=None):

        if position_y == None:
            position_y = self.position_y_default

        self.__build_image_card(0, position_x, position_y, 1) # player[0] = rank_card
                                                             # player[1] = suit_card

    def second_card(self,position_x=90, position_y=None):

        if position_y == None:
            position_y = self.position_y_default

        self.__build_image_card(1,position_x, position_y, 2) # player[1] = rank_card
                                                             # player[1] = suit_card

    def third_card(self,position_x=180, position_y=None):

        if position_y == None:
            position_y = self.position_y_default

        self.__build_image_card(2,position_x, position_y, 3) # player[3] = rank_card
                                                             # player[1] = suit_card

    def fourth_card(self,position_x=270, position_y=None):

        if position_y == None:
            position_y = self.position_y_default

        self.__build_image_card(3,position_x, position_y, 4) # player[4] = rank_card
                                                             # player[1] = suit_card

    def fifth_card(self,position_x=360, position_y=None):

        if position_y == None:
            position_y = self.position_y_default

        self.__build_image_card(4,position_x, position_y, 5) # player[5] = rank_card
                                                             # player[1] = suit_card

    def sixth_card(self,position_x=450, position_y=None):

        if position_y == None:
            position_y = self.position_y_default

        self.__build_image_card(5,position_x, position_y, 6) # player[6] = rank_card
                                                             # player[1] = suit_card

    def seventh_card(self,position_x=540, position_y=None):

        if position_y == None:
            position_y = self.position_y_default

        self.__build_image_card(6,position_x, position_y, 7) # player[7] = rank_card
                                                             # player[1] = suit_card

    def eighth_card(self,position_x=630, position_y=None):

        if position_y == None:
            position_y = self.position_y_default

        self.__build_image_card(7,position_x, position_y, 8) # player[8] = rank_card
                                                             # player[1] = suit_card

    def nineth_card(self,position_x=720, position_y=None):

        if position_y == None:
            position_y = self.position_y_default

        self.__build_image_card(8,position_x, position_y, 9) # player[9] = rank_card
                                                             # player[1] = suit_card


    def first_card_clicked(self, event=None):
        self.__card_clicked(1)

    def second_card_clicked(self, event=None):
        self.__card_clicked(2)

    def third_card_clicked(self, event=None):
        self.__card_clicked(3)

    def fourth_card_clicked(self, event=None):
        self.__card_clicked(4)

    def fifth_card_clicked(self, event=None):
        self.__card_clicked(5)

    def sixth_card_clicked(self, event=None):
        self.__card_clicked(6)

    def seventh_card_clicked(self, event=None):
        self.__card_clicked(7)

    def eighth_card_clicked(self, event=None):
        self.__card_clicked(8)

    def nineth_card_clicked(self, event=None):
        self.__card_clicked(9)

