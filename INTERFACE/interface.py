from INTERFACE.image_generator import *
from INTERFACE.directories import *
from INTERFACE.background import Background as bck
from INTERFACE.player_deck import *
from INTERFACE.general_deck import *
from main import deck
from player import player_cards, change_order_cards

class Interface:
    def __init__(self, master=None):
        self.master = master

        self.__init_bck()
        self.__init_back_cards()
        self.__init_player_deck()

    def __init_bck(self):
        bck(self.master)

    def __init_back_cards(self):
        Deck_Cards(self.master)

    def __init_player_deck(self):
        Player_Deck(self.master)




root = Tk()
Interface(root)
root.mainloop()