'''MODULES AND FUNCTIONS IMPORTED'''
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

from main import deck
from player import player_cards, change_order_cards


# MAC OS
# file_cards = os.getcwd() + '/cards/'
# file_img = os.getcwd() + '/img/'

# WINDOWS OS
file_cards = os.getcwd() + '\cards\\'
file_img = os.getcwd() + '\img\\'

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

        w = int(ws * 0.80)  # width for the Tk root
        h = int(ws * 0.40)  # height for the Tk root

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

    def __init__(self, master):
        super().__init__(master)

class Deck_Cards(Img):

    deck_showing_card = False

    def __init__(self, master):
        super().__init__(master)
        self.deck_module()

    def deck_module(self, file_image=None, position_x=400, position_y=150):

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

    def __init_bck(self):
        Background(self.master)

    def __init_back_cards(self):
        Deck_Cards(self.master)




root = Tk()
Interface(root)
root.mainloop()