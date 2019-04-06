import os
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

from player import player_cards
from main import deck

file = os.getcwd() + '/cards/' # MAC
# file = os.getcwd() + '\cards\\' # windows

class Application:

    deck_showing_card = False

    def __init__(self, master=None):
        self.image_deck = Button(root, image=self.show_deck_cards(), command=self.deck_clicked)
        self.player_card_first = None
        self.player_card_second = None
        self.player_card_third = None
        self.player_card_fourth = None
        self.player_card_fifth = None
        self.player_card_sixth = None
        self.player_card_seventh = None
        self.player_card_eighth = None
        self.player_card_nineth = None

    def open_img(self, file_image, position_x, position_y, size_x=180,
                 size_y=250, angulo=0):

        img = Image.open(file_image)
        img = img.resize((size_x, size_y), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img.rotate(angulo))
        panel = Label(root, image=img)
        panel.image = img
        panel.place(x=position_x, y=position_y)

    def show_deck_cards(self, name_card=None):
        if name_card == None:
            name_card = 'BACK_CARD.png'
        self.open_img((file + name_card), 350, 100)

    def deck_clicked(self):

        # del self.image_deck

        if len(deck) > 0:
            if self.deck_showing_card == False:
                name = deck[0][0] + '_' + deck[0][1] + '.png'
                del deck[0]
                self.show_deck_cards((file + name))
                self.deck_showing_card = True

            else:
                name = 'BACK_CARD.png'
                self.show_deck_cards((file + name))
                self.deck_showing_card = False


class Deck(Application):

    def __init__(self, master=None):
        super().__init__(self)










root = Tk()
Application(root)
root.geometry("1000x700+300+150")
root.resizable(width=True, height=True)
root.title('PIF GAME')








root.mainloop()