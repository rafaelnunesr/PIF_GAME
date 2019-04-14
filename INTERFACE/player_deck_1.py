from INTERFACE.directories import *
from INTERFACE.image_generator import *
from player import *

function_card_names = ['first', 'second', 'third',
                       'fourth', 'fifth', 'sixth',
                       'seventh', 'eighth', 'nineth'
                                                    ]

class Player_Deck(Img):

    display_info_player = {
                           x: [False, None, ''.join('self.' + function_card_names[x - 1] + '_card'),
                           ''.join('self.' + function_card_names[x - 1] + '_card_clicked')]
                           for x in range (1,10)
                                                }

    def __init__(self, master):
        super().__init__(master)
        self.position_y_default = 380
        self.__card_game_positions()

    def __card_game_positions(self):
        for card_number in range(1,10):
            func = eval(self.display_info_player[card_number][2])
            if self.display_info_player[card_number][0]:
                func(position_y=300)

            else:
                func()

    def __change_card(self, number):
        change_order_cards(self.first_card_selected, number)

    def __build_image_card(self, card_position_list, position_x, position_y, card_clicked):

        func = eval(self.display_info_player[card_clicked][3])

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

