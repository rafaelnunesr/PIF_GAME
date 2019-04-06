import os
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

from player import player_cards
from main import deck

file = os.getcwd() + '/cards/' # MAC
# file = os.getcwd() + '\cards\\' # windows

class Application:

    def __init__(self, master=None):
        pass








root = Tk()
Application(root)
root.geometry("1000x700+300+150")
root.resizable(width=True, height=True)
root.title('PIF GAME')








root.mainloop()