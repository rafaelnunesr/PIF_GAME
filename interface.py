'''MODULES AND FUNCTIONS IMPORTED'''
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

from main import deck
from player import player_cards, change_order_cards


# MAC OS
file_cards = os.getcwd() + '/cards/'
file_img = os.getcwd() + '/img/'

# WINDOWS OS
# file_cards = os.getcwd() + '\cards\\'
# file_img = os.getcwd() + '\img\\'

class Img:

    def __init__(self, master=None):
        self.master = master

    def show_image(self, file_image, size_x=180, size_y=250, angle=0):
        '''Receives file name, sizes, and angle from each image'''
        img = Image.open(file_image).convert("RGBA")
        img = img.resize((size_x, size_y), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img.rotate(angle))
        return img

class Background(Img):

    def __init__(self, master=None):
        super().__init__(master)

        w, h = self.__window_configuration()
        self.__background_image(w, h)
        self.__load_logo()

    def __window_configuration(self):
        '''Setup window size Tk'''
        self.master.winfo_width()

        ws, hs = self.__get_window_size()

        # w = int(ws * 0.80)  # width for the Tk root
        # h = int(ws * 0.40)  # height for the Tk root

        w = 1000
        h = 800

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.master.resizable(width=True, height=True)
        self.master.title('PIF GAME')
        return w, h

    def __get_window_size(self):
        '''get screen width and height from user'''
        ws = self.master.winfo_screenwidth()  # width of the screen
        hs = self.master.winfo_screenheight()  # height of the screen
        return  [ws, hs]

    def __background_image(self, w, h):
        '''Load background image'''
        name_backgound = file_img + 'PIF_BACKGROUND.jpg'

        img = self.show_image(name_backgound, w, h)
        bck_panel = Label(self.master, image=img)
        bck_panel.image = img
        bck_panel.pack()

    def __load_logo(self):
        '''Load logo image'''
        logo = file_img + 'PIF_LOGO.png'

        img = self.show_image(logo,250,80)
        logo_panel = Label(self.master, image=img)
        logo_panel.image = img
        logo_panel.place(x=20, y=20)

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



    def __build_image_card(self,rank_card, suit_card, position_x, position_y, card_clicked):
        global card_panel
        cards = {1:'self.first_card_clicked', 2:'self.second_card_clicked',
                 3:'self.third_card_clicked', 4:'self.fourth_card_clicked',
                 5:'self.fifth_card_clicked', 6:'self.sixth_card_clicked',
                 7:'self.seventh_card_clicked', 8:'self.eighth_card_clicked',
                 9:'self.nineth_card_clicked'}

        func = eval(cards[card_clicked])

        card_name = player_cards[rank_card][0] + '_' + player_cards[suit_card][1] + '.png'
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

        self.__build_image_card(0, 1, position_x, position_y, 1) # player[0] = rank_card
                                                 # player[1] = suit_card

    def first_card_clicked(self, event=None):
        if self.display_info_player[1]:
            self.display_info_player[1] = False
        else:
            self.display_info_player[1] = True

        self.__destroy_cards()
        self.__card_game_positions()

    def second_card(self, position_x=90, position_y=None):

        if position_y == None:
            position_y = self.position_y_default

        self.__build_image_card(1, 1, position_x, position_y, 2) # player[0] = rank_card
                                                 # player[1] = suit_card

    def second_card_clicked(self, event=None):
        print('Rafa')

class Deck_Cards(Img):

    deck_showing_card = False

    def __init__(self, master):
        super().__init__(master)
        self.deck_module()

    def deck_module(self, file_image=None, position_x=350, position_y=80):

        if file_image == None:
            file_image = ''.join(file_cards + 'BACK_CARD.png')

        img = self.show_image(file_image)
        deck_panel = Button(self.master, image=img, borderwidth=0)
        deck_panel.image = img
        deck_panel.bind('<Button-1>', self.deck_clicked)
        deck_panel.place(x=position_x, y=position_y)

    def deck_clicked(self, event=None):

        if len(deck) > 0:
            if self.deck_showing_card == False:
                name = deck[0][0] + '_' + deck[0][1] + '.png'
                del deck[0]
                self.deck_module((file_cards + name))
                self.deck_showing_card = True

            else:
                self.deck_module()
                self.deck_showing_card = False

        else:
            file_image = ''.join(file_cards + 'END_DECK.png')
            self.deck_module(file_image)

class Interface:
    def __init__(self, master=None):
        self.master = master

        self.__init_bck()
        self.__init_back_cards()
        self.__init_player_deck()

    def __init_bck(self):
        Background(self.master)

    def __init_back_cards(self):
        Deck_Cards(self.master)

    def __init_player_deck(self):
        Player_Deck(self.master)




root = Tk()
Interface(root)
root.mainloop()