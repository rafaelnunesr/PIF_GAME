import tkinter as tk

def generate_buttons(n):
    for _ in range(n):              #   xrange in python 2
        newbutton = tk.Button(text=_, command=lambda name=_: change_relief(name))
        newbutton.grid(column=_)
        buttons.append(newbutton)


def change_relief(idx):
    button = buttons[idx]

    if button['relief'] == 'raised':
        button.config(relief='sunken')
    else:
        button.config(relief='raised')


root = tk.Tk()

#   our list with buttons
buttons = []

#   generate some buttons
generate_buttons(5)

#   another button, that uses a value from an entry below
change_relief_button = tk.Button(text='Change relief by id',
                                 command=lambda: change_relief(int(id_entry.get())))
change_relief_button.grid()

#   entry with user input
id_entry = tk.Entry()
id_entry.grid()

#   default 0
id_entry.insert(0, '0')

print(buttons)

#   mainloop
root.mainloop()