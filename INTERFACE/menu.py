from tkinter import Menu


class Menu_Bar:

    def __init__(self, master):
        self.master = master
        self.__menu()


    def __menu(self):
        menubar = Menu(self.master)
        menubar.add_command(label="Quit!", command=self.master.quit)

        # display the menu
        self.master.config(menu=menubar)