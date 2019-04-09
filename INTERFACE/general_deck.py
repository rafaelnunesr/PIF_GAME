from INTERFACE.image_generator import *
from INTERFACE.directories import *
from main import *

class Deck_Cards(Img):

    deck_showing_card = False
    card_in_bin = None

    def __init__(self, master):
        super().__init__(master)
        self.deck_module()

    def deck_module(self, file_image=None, position_x=350, position_y=80):
        global deck_panel
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
                self.__destroy_deck()
                self.card_in_bin = name
                self.deck_module((file_cards + name))
                self.deck_showing_card = True

            '''else:
                self.deck_module()
                self.deck_showing_card = False'''
            self.__buttoms_accept_reject()

        else:
            file_image = ''.join(file_cards + 'END_DECK.png')
            self.deck_module(file_image)

    def __buttoms_accept_reject(self):
        global accept_panel, reject_panel
        accept_buttom = file_img + 'ACCEPT.png'
        reject_buttom = file_img + 'REJECT.png'

        img_accept = self.show_image(accept_buttom, 60,60)
        accept_panel = Button(self.master, image=img_accept, highlightthickness = 0, bd = 0)
        accept_panel.image = img_accept
        accept_panel.bind('<Button-1>', self.card_accepted)
        accept_panel.place(x=365, y=10)

        img_reject = self.show_image(reject_buttom, 60,60)
        reject_panel = Button(self.master, image=img_reject, highlightthickness = 0, bd = 0)
        reject_panel.image = img_reject
        reject_panel.bind('<Button-1>', self.card_rejected)
        reject_panel.place(x=440, y=10)

    def card_accepted(self, event=None):
        print('accepted')

    def card_rejected(self, event=None):
        self.deck_module()
        self.deck_showing_card = False
        self.bin()
        self.__destroy_buttoms()

    def __destroy_buttoms(self):
        global accept_panel, reject_panel
        accept_panel.destroy()
        reject_panel.destroy()

    def __destroy_deck(self):
        global deck_panel
        deck_panel.destroy()

    def bin(self):
        if self.card_in_bin != None:
            print('running')
            file_image = file_cards + self.card_in_bin
            img = self.show_image(file_image)
            bin_panel = Button(self.master, image=img, borderwidth=0)
            bin_panel.image = img
            bin_panel.bind('<Button-1>', self.deck_clicked)
            bin_panel.place(x=600, y=80)