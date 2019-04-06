from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

from collections import defaultdict

from player import player_cards
from main import deck



file = os.getcwd() + '/cards/' # MAC
# file = os.getcwd() + '\cards\\' # windows

root = Tk()
root.geometry("1000x700+300+150")
root.resizable(width=True, height=True)
root.title('PIF GAME')



'''
def open_img(file_image, position_x, position_y, size_x=180,
             size_y=250, angulo=0):

    img = Image.open(file_image)
    img = img.resize((size_x,size_y), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img.rotate(angulo))
    panel = Label(root, image=img)
    panel.image = img
    panel.place(x=position_x, y=position_y)'''

def open_img(file_image, position_x, position_y, size_x=180,
             size_y=250, angulo=0):

    img = Image.open(file_image)
    img = img.resize((size_x,size_y), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img.rotate(angulo))
    panel = Button(root, image=img)
    panel.image = img
    panel.bind('<Button-1>', on_click)
    panel.place(x=position_x, y=position_y)

def fist_card(file_image, position_x=0, position_y=400, size_x=180,
             size_y=250, angulo=0):

    img = Image.open(file_image)
    img = img.resize((size_x,size_y), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img.rotate(angulo))
    panel_1 = Button(root, image=img)
    panel_1.image = img
    panel_1.bind('<Button-1>', first_card_clicked)
    panel_1.place(x=position_x, y=position_y)

def second_card(file_image, position_x=0, position_y=400, size_x=180,
             size_y=250, angulo=0):

    img = Image.open(file_image)
    img = img.resize((size_x,size_y), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img.rotate(angulo))
    panel_2 = Button(root, image=img)
    panel_2.image = img
    panel_2.bind('<Button-1>', second_card_clicked)
    panel_2.place(x=position_x, y=position_y)

def third_card(file_image, position_x=0, position_y=400, size_x=180,
             size_y=250, angulo=0):

    img = Image.open(file_image)
    img = img.resize((size_x,size_y), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img.rotate(angulo))
    panel_3 = Button(root, image=img)
    panel_3.image = img
    panel_3.bind('<Button-1>', third_card_clicked)
    panel_3.place(x=position_x, y=position_y)

'''def show_cards_tkinter():
    name_card = 'BACK_CARD.png'
    open_img((file + name_card), 350, 100)

    position_x = 0
    x = 0

    for e in range (9):
        name_card = player_cards[x][0] + '_' +  player_cards[x][1] + '.png'
        open_img((file + name_card), position_x, 400)
        position_x += 90
        x += 1'''

def show_deck(file_image, position_x, position_y, size_x = 180,
              size_y = 250, angulo = 0):

    img = Image.open(file_image)
    img = img.resize((size_x, size_y), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img.rotate(angulo))
    panel_1 = Button(root, image=img)
    panel_1.image = img
    panel_1.bind('<Button-1>', deck_clicked)
    panel_1.place(x=position_x, y=position_y)

def show_cards_tkinter():
    name_card = 'BACK_CARD.png'
    show_deck((file + name_card), 350, 100)

    position_x = 0
    x = 0

    name_card = name_card = player_cards[0][0] + '_' +  player_cards[0][1] + '.png'
    fist_card((file + name_card), position_x, 400)

    name_card = name_card = player_cards[1][0] + '_' + player_cards[1][1] + '.png'
    second_card((file + name_card), position_x + 90, 400)

    name_card = name_card = player_cards[3][0] + '_' + player_cards[3][1] + '.png'
    third_card((file + name_card), position_x + 180, 400)

    '''
    

    for e in range (9):
        name_card = player_cards[x][0] + '_' +  player_cards[x][1] + '.png'
        open_img((file + name_card), position_x, 400)
        position_x += 90
        x += 1'''

deck_showing_card = False

def deck_clicked(event=None):

    global deck_showing_card

    if len(deck) > 0:
        if deck_showing_card == False:
            name = deck[0][0] + '_' +  deck[0][1] + '.png'
            del deck[0]
            show_deck((file + name), 350, 100)
            deck_showing_card = True


        else:
            name = 'BACK_CARD.png'
            show_deck((file + name), 350, 100)
            deck_showing_card = False




def first_card_clicked(event=None):
    position_x = 0
    name_card = name_card = player_cards[0][0] + '_' + player_cards[0][1] + '.png'
    fist_card((file + name_card), position_x, 380)

    position_x = 90
    name_card = name_card = player_cards[1][0] + '_' + player_cards[1][1] + '.png'
    second_card((file + name_card), position_x, 400)

    position_x = 180
    name_card = name_card = player_cards[2][0] + '_' + player_cards[2][1] + '.png'
    third_card((file + name_card), position_x, 400)



def second_card_clicked(event=None):
    position_x = 0
    name_card = name_card = player_cards[0][0] + '_' + player_cards[0][1] + '.png'
    fist_card((file + name_card), position_x, 400)

    position_x = 90
    name_card = name_card = player_cards[1][0] + '_' + player_cards[1][1] + '.png'
    second_card((file + name_card), position_x, 380)

    position_x = 180
    name_card = name_card = player_cards[2][0] + '_' + player_cards[2][1] + '.png'
    third_card((file + name_card), position_x, 400)

def third_card_clicked(event=None):
    position_x = 0
    name_card = name_card = player_cards[0][0] + '_' + player_cards[0][1] + '.png'
    fist_card((file + name_card), position_x, 400)

    position_x = 90
    name_card = name_card = player_cards[1][0] + '_' + player_cards[1][1] + '.png'
    second_card((file + name_card), position_x, 400)

    position_x = 180
    name_card = name_card = player_cards[2][0] + '_' + player_cards[2][1] + '.png'
    third_card((file + name_card), position_x, 380)

def on_click(event=None):
    print('card_clicked')

show_cards_tkinter()

root.mainloop()

