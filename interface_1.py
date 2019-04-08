from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

from main import deck
from player import player_cards


file = os.getcwd() + '/cards/' # MAC
# file = os.getcwd() + '\cards\\' # windows

class Interface:

    deck_showing_card = False
    player_first_card_up = False
    player_second_card_up = False
    player_third_card_up = False
    player_fourth_card_up = False
    player_fifth_card_up = False
    player_sixth_card_up = False
    player_seventh_card_up = False
    player_eighth_card_up = False
    player_nineth_card_up = False

    player_cards_position_y = 380
    player_cards_position_up = 300

    def __init__(self, master=None):
        self.master = master
        self.master.geometry("1000x700+300+150")
        self.master.resizable(width=True, height=True)
        self.master.title('PIF GAME')

        self.cards_deck = self.deck_module()
        self.__card_game_positions()


    def __card_game_positions(self, first=380, second=380, third=380,
                              fourth=380, fifth=380, sixth=380, seventh=380,
                              eighth=380, nineth=380):

        self.player_first_card = self.first_card(0, first)
        self.player_second_card = self.second_card(90, second)
        self.player_third_card = self.third_card(180, third)
        self.player_fourth_card = self.fourth_card(270, fourth)
        self.player_fifth_card = self.fifth_card(360, fifth)
        self.player_sixth_card = self.sixth_card(450, sixth)
        self.player_seventh_card = self.seventh_card(540, seventh)
        self.player_eighth_card = self.eighth_card(630, eighth)
        self.player_nineth_card = self.nineth_card(720, nineth)


    def show_image(self, file_image, position_x, position_y, size_x=180,
                   size_y=250, angulo=0):

        img = Image.open(file_image)
        img = img.resize((size_x, size_y), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img.rotate(angulo))
        return img


    def deck_module(self, file_image=None, position_x=350, position_y=100):

        if file_image == None:
            file_image = ''.join(file + 'BACK_CARD.png')

        img = self.show_image(file_image, position_x, position_y)
        deck_panel = Button(self.master, image=img)
        deck_panel.image = img
        deck_panel.bind('<Button-1>', self.deck_clicked)
        deck_panel.place(x=position_x, y=position_y)

    def deck_clicked(self, event=None):

        if len(deck) > 0:
            if self.deck_showing_card == False:
                name = deck[0][0] + '_' + deck[0][1] + '.png'
                del deck[0]
                self.deck_module((file + name))
                self.deck_showing_card = True

            else:
                self.deck_module()
                self.deck_showing_card = False

        else:
            self.deck_module()


    def first_card(self, position_x, position_y):
        global first_panel
        card_name = player_cards[0][0] + '_' + player_cards[0][1] + '.png'
        file_image = file + card_name

        img = self.show_image(file_image, position_x, position_y)

        first_panel = Button(self.master, image=img)
        first_panel.image = img
        first_panel.bind('<Button-1>', self.first_card_clicked)
        first_panel.place(x=position_x, y=position_y)


    def first_card_clicked(self, event=0):
        global first_panel
        first_panel.destroy()

        position_x = 0

        if self.player_first_card_up == False:
            self.__card_game_positions(first=self.player_cards_position_up)
            self.player_first_card_up = True
        else:
            self.__card_game_positions()
            self.player_first_card_up = False


    def second_card(self, position_x, position_y):
        global second_panel
        card_name = player_cards[1][0] + '_' + player_cards[1][1] + '.png'
        file_image = file + card_name

        img = self.show_image(file_image, position_x, position_y)
        second_panel = Button(self.master, image=img)
        second_panel.image = img
        second_panel.bind('<Button-1>', self.second_card_clicked)
        second_panel.place(x=position_x, y=position_y)

    def second_card_clicked(self, event=0):
        global second_panel
        second_panel.destroy()

        position_x = 90

        if self.player_second_card_up == False:
            self.__card_game_positions(second=self.player_cards_position_up)
            self.player_second_card_up = True
        else:
            self.__card_game_positions()
            self.player_second_card_up = False

    def third_card(self, position_x, position_y):
        global third_panel

        card_name = player_cards[2][0] + '_' + player_cards[2][1] + '.png'
        file_image = file + card_name

        img = self.show_image(file_image, position_x, position_y)
        third_panel = Button(self.master, image=img)
        third_panel.image = img
        third_panel.bind('<Button-1>', self.third_card_clicked)
        third_panel.place(x=position_x, y=position_y)

    def third_card_clicked(self, event=0):
        global third_panel
        third_panel.destroy()

        position_x = 180

        if self.player_third_card_up == False:
            self.__card_game_positions(third=self.player_cards_position_up)
            self.player_third_card_up = True
        else:
            self.__card_game_positions()
            self.player_third_card_up = False

    def fourth_card(self, position_x, position_y):
        global fourth_panel
        card_name = player_cards[3][0] + '_' + player_cards[3][1] + '.png'
        file_image = file + card_name

        img = self.show_image(file_image, position_x, position_y)
        fourth_panel = Button(self.master, image=img)
        fourth_panel.image = img
        fourth_panel.bind('<Button-1>', self.fourth_card_clicked)
        fourth_panel.place(x=position_x, y=position_y)

    def fourth_card_clicked(self, event=0):

        global fourth_panel
        fourth_panel.destroy()

        position_x = 270

        if self.player_fourth_card_up == False:
            self.__card_game_positions(fourth=self.player_cards_position_up)
            self.player_fourth_card_up = True
        else:
            self.__card_game_positions()
            self.player_fourth_card_up = False

    def fifth_card(self, position_x, position_y):
        global fifth_panel
        card_name = player_cards[4][0] + '_' + player_cards[4][1] + '.png'
        file_image = file + card_name

        img = self.show_image(file_image, position_x, position_y)
        fifth_panel = Button(self.master, image=img)
        fifth_panel.image = img
        fifth_panel.bind('<Button-1>', self.fifth_card_clicked)
        fifth_panel.place(x=position_x, y=position_y)

    def fifth_card_clicked(self, event=0):
        global fifth_panel
        fifth_panel.destroy()

        position_x = 360

        if self.player_fifth_card_up == False:
            self.__card_game_positions(fifth=self.player_cards_position_up)
            self.player_fifth_card_up = True
        else:
            self.__card_game_positions()
            self.player_fifth_card_up = False

    def sixth_card(self, position_x, position_y):
        global sixth_panel
        card_name = player_cards[5][0] + '_' + player_cards[5][1] + '.png'
        file_image = file + card_name

        img = self.show_image(file_image, position_x, position_y)
        sixth_panel = Button(self.master, image=img)
        sixth_panel.image = img
        sixth_panel.bind('<Button-1>', self.sixth_card_clicked)
        sixth_panel.place(x=position_x, y=position_y)

    def sixth_card_clicked(self, event=0):
        global sixth_panel
        sixth_panel.destroy()

        position_x = 450

        if self.player_sixth_card_up == False:
            self.__card_game_positions(sixth=self.player_cards_position_up)
            self.player_sixth_card_up = True
        else:
            self.__card_game_positions()
            self.player_sixth_card_up = False

    def seventh_card(self, position_x, position_y):
        global seventh_panel
        card_name = player_cards[6][0] + '_' + player_cards[6][1] + '.png'
        file_image = file + card_name


        img = self.show_image(file_image, position_x, position_y)
        seventh_panel = Button(self.master, image=img)
        seventh_panel.image = img
        seventh_panel.bind('<Button-1>', self.seventh_card_clicked)
        seventh_panel.place(x=position_x, y=position_y)

    def seventh_card_clicked(self, event=0):
        global seventh_panel
        seventh_panel.destroy()

        position_x = 540

        if self.player_seventh_card_up == False:
            self.__card_game_positions(seventh=self.player_cards_position_up)
            self.player_seventh_card_up = True
        else:
            self.__card_game_positions()
            self.player_seventh_card_up = False

    def eighth_card(self, position_x, position_y):
        global eighth_panel
        card_name = player_cards[7][0] + '_' + player_cards[7][1] + '.png'
        file_image = file + card_name

        img = self.show_image(file_image, position_x, position_y)
        eighth_panel = Button(self.master, image=img)
        eighth_panel.image = img
        eighth_panel.bind('<Button-1>', self.eighth_card_clicked)
        eighth_panel.place(x=position_x, y=position_y)

    def eighth_card_clicked(self, event=0):
        global eighth_panel
        eighth_panel.destroy()

        position_x = 630

        if self.player_eighth_card_up == False:
            self.__card_game_positions(eighth=self.player_cards_position_up)
            self.player_eighth_card_up = True
        else:
            self.__card_game_positions()
            self.player_eighth_card_up = False

    def nineth_card(self, position_x, position_y):
        global nineth_panel
        card_name = player_cards[8][0] + '_' + player_cards[8][1] + '.png'
        file_image = file + card_name

        img = self.show_image(file_image, position_x, position_y)
        nineth_panel = Button(self.master, image=img)
        nineth_panel.image = img
        nineth_panel.bind('<Button-1>', self.nineth_card_clicked)
        nineth_panel.place(x=position_x, y=position_y)

    def nineth_card_clicked(self, event=0):
        global nineth_panel
        nineth_panel.destroy()

        position_x = 720

        if self.player_nineth_card_up == False:
            self.__card_game_positions(nineth=self.player_cards_position_up)
            self.player_nineth_card_up = True
        else:
            self.__card_game_positions()
            self.player_nineth_card_up = False


root = Tk()
Interface(root)
root.mainloop()