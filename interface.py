from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os


from player import player_cards



file = os.getcwd() + '\cards\\'

root = Tk()
root.geometry("1000x300+300+150")
root.resizable(width=True, height=True)
root.title('PIF GAME')

def open_img(file_image, side_1, side_2, angulo=0):
    global canvas
    img = Image.open(file_image)
    img = img.resize((180,250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img.rotate(angulo))
    panel = Label(root, image=img)
    panel.image = img
    panel.place(x=side_1, y=side_2)

def show_cards_tkinter():
    side = 0
    x = 0

    for e in range (9):
        name_card = player_cards[x][0] + '_' +  player_cards[x][1] + '.png'
        open_img((file + name_card), side,1)
        side += 90
        x += 1


show_cards_tkinter()

root.mainloop()


