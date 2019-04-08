'''MODULES AND FUNCTIONS IMPORTED'''
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

from main import deck
from player import player_cards, change_order_cards


# file = os.getcwd() + '/cards/' # MAC OS
file = os.getcwd() + '\cards\\' # WINDOWS OS

class Interface:

    def __init__(self, master=None):
        self.master = master
        w, h = self.__window_configuration()
        self.__background_image(w, h)
        self.__load_logo()

    def __window_configuration(self):
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
        # get screen width and height
        ws = self.master.winfo_screenwidth()  # width of the screen
        hs = self.master.winfo_screenheight()  # height of the screen
        return  [ws, hs]

    def __background_image(self, w, h):
        name_backgound = ''.join(os.getcwd() + '\img\\' + 'PIF_BACKGROUND.jpg') # Windows OS
        # name_backgound = ''.join(os.getcwd() + '/img/' + 'PIF_BACKGROUND.jpg') # MAC OS

        img = self.show_image(name_backgound, w, h)

        panel = Label(self.master, image=img)
        panel.image = img
        panel.pack()

    def __load_logo(self):
        logo = ''.join(os.getcwd() + '\img\\' + 'PIF_LOGO.png') # Windows OS
        # logo = ''.join(os.getcwd() + '/img/' + 'PIF_LOGO.png') # MAC OS

        img = self.show_image(logo,250,80)
        panel = Label(self.master, image=img)
        panel.image = img
        panel.place(x=20, y=20)

    def show_image(self, file_image, size_x=180, size_y=250, angulo=0):

        img = Image.open(file_image).convert("RGBA")
        img = img.resize((size_x, size_y), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img.rotate(angulo))
        return img


root = Tk()
Interface(root)
root.mainloop()