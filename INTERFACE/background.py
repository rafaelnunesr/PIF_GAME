from INTERFACE.directories import *
from INTERFACE.image_generator import *

class Background(Img):

    def __init__(self, master=None):
        super().__init__(master)

        w, h = self.__window_configuration()
        self.__background_image(w, h)
        self.__load_logo()

    def __window_configuration(self):
        '''Setup window size Tk'''
        self.master.winfo_width()

        ws, hs = self.__get_window_size()

        # w = int(ws * 0.80)  # width for the Tk root
        # h = int(ws * 0.40)  # height for the Tk root

        w = 1000
        h = 800

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
        '''get screen width and height from user'''
        ws = self.master.winfo_screenwidth()  # width of the screen
        hs = self.master.winfo_screenheight()  # height of the screen
        return  [ws, hs]

    def __background_image(self, w, h):
        '''Load background image'''
        name_backgound = file_img + 'PIF_BACKGROUND.jpg'

        img = self.show_image(name_backgound, w, h)
        bck_panel = Label(self.master, image=img)
        bck_panel.image = img
        bck_panel.pack()

    def __load_logo(self):
        '''Load logo image'''
        logo = file_img + 'PIF_LOGO.png'

        img = self.show_image(logo,250,70)
        logo_panel = Label(self.master, image=img, borderwidth=0)
        logo_panel.image = img
        logo_panel.place(x=20, y=20)

