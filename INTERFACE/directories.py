import os

try:
    # MAC OS
    file_cards = os.getcwd() + '/CARDS/'
    file_img = os.getcwd() + '/IMG/'

except FileNotFoundError:

    # WINDOWS OS
    file_cards = os.getcwd() + '\CARDS\\'
    file_img = os.getcwd() + '\IMG\\'
