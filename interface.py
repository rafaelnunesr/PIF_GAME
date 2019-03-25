from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

arquivo = os.getcwd() + '\cards\\' + 'A_CLUBS.png'

root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)


def open_img(side_1, side_2, angulo=0):
    x = arquivo
    img = Image.open(x)
    img = img.resize((180,250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img.rotate(angulo))
    panel = Label(root, image=img,)
    panel.image = img
    panel.place(x=side_1, y=side_2)

side = 0
for e in range (9):
    open_img(side,1)
    side += 90




root.mainloop()


