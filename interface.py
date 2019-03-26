from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os


from player import *


file = os.getcwd() + '\cards\\' # Windows
# file = os.getcwd() + '/cards/' # MAC

root = Tk()
root.geometry("1000x700+300+150")
root.resizable(width=True, height=True)
root.title('PIF GAME')


def open_img(card_image, position_x, position_y, size_x=180,
             size_y=250, angulo=0):

    img = Image.open(card_image)
    img = img.resize((size_x,size_y), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img.rotate(angulo))
    panel = Label(root, image=img)
    panel.image = img
    panel.place(x=position_x, y=position_y)

def show_player_cards_tkinter():

    position_x = 0
    x = 0

    for e in range (9):
        name_card = player_cards[x][0] + '_' +  player_cards[x][1] + '.png'
        open_img((file + name_card), position_x,400)
        position_x += 90
        x += 1

def show_deck_cards():
    img_deck_card = 'BACK_CARD.png'
    open_img((file + img_deck_card), 350, 100)


def ask_deck_card():

    next_card = deck[0]
    del deck[0]
    next_card = next_card[0] + '_' + next_card[1] + '.png'
    img_deck_card = next_card
    open_img((file + img_deck_card), 350, 100)


show_deck_cards()
show_player_cards_tkinter()


root.mainloop()


