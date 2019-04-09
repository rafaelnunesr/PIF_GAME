'''MODULES AND FUNCTIONS IMPORTED'''
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

class Img:

    def __init__(self, master=None):
        self.master = master

    def show_image(self, file_image, size_x=180, size_y=250, angle=0):
        '''Receives file name, sizes, and angle from each image'''
        img = Image.open(file_image).convert("RGBA")
        img = img.resize((size_x, size_y), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img.rotate(angle))
        return img