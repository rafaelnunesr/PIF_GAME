from INTERFACE.directories import *
from INTERFACE.image_generator import *
from player import *


class Player_Deck(Img):

    display_info_player = {
                           x: {'UP': False, 'BUTTOM': None}
                                            for x in range(1, 10)
                                                                      }

    def __init__(self, master):
        super().__init__(master)
        self.__card_game_positions()

    def __card_game_positions(self):
        for number in range(1, 10):
            if self.display_info_player[number]['UP']:
                self.build_card(card_number=number,
                                position_x=(number-1)*90,
                                position_y=300)

            else:
                self.build_card(card_number=number,
                                position_x=(number-1)*90)

    def __build_image_card(self, card_position_list,
                           position_x, position_y):
        global card_num
        card_num = card_position_list + 1

        card_name = player_cards[card_position_list][0] + '_' \
                    + player_cards[card_position_list][1] + '.png'

        file_image = file_cards + card_name

        img = self.show_image(file_image)
        card_panel = Button(self.master, image=img, highlightthickness=0)
        card_panel.image = img
        card_panel.bind('<Button-1>', self.__call_func_card)
        card_panel.place(x=position_x, y=position_y)
        self.display_info_player[card_num]['BUTTOM'] = card_panel
        print(self.display_info_player)

    def __call_func_card(self, event=None):
        global card_num
        return self.__card_clicked(card_num)

    def __destroy_cards(self):
        for x in range(1,10):
            self.display_info_player[x]['BUTTOM'].destroy()

    def __card_clicked(self, position):

        if self.display_info_player[position]['UP']:
            self.display_info_player[position]['UP'] = False
        else:
            self.display_info_player[position]['UP'] = True

        self.__destroy_cards()
        self.__card_game_positions()

    def build_card(self, card_number, position_x, position_y=None):

        if position_y == None:
            position_y = 380

        self.__build_image_card(card_number - 1, position_x, position_y)


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

