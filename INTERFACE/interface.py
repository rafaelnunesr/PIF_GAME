from INTERFACE.image_generator import *
from INTERFACE.directories import *
from INTERFACE.background import Background as bck
from INTERFACE.player_deck import *
from INTERFACE.general_deck import *
from INTERFACE.menu import *
from main import deck
from player import player_cards, change_order_cards

class Interface:
    def __init__(self, master=None):
        self.master = master

        self.init_bck()
        self.init_back_cards()
        self.init_player_deck()

    def init_bck(self):
        bck(self.master)

    def init_back_cards(self):
        Deck_Cards(self.master)

    def init_player_deck(self):
        Player_Deck(self.master)

    def init_menu(self):
        Menu_Bar(self.master)


root = Tk()
Interface(root)
root.mainloop()