try:
    from tkinter import *
except ImportError:
    from Tkinter import *
import tkinterweb
from PIL import ImageTk

### IMPORT BUTTONS ###
from src import Background
from src.buttons.CreateAccountLink import CreateAccountLink
from src.buttons.ForgotPasswordLink import ForgotPasswordLink
from src.buttons.ManageAccountLink import ManageAccountLink
from src.buttons.PlayButton import PlayButton
from src.buttons.ReportABugButton import ReportABugButton
from src.buttons.PlayersGuideButton import PlayersGuideButton
from src.buttons.HomepageButton import HomepageButton
from src.buttons.TopToonsButton import TopToonsButton
from src.buttons.GraphicOptionsButton import GraphicOptionsButton
from src.buttons.QuitButton import QuitButton
from src.buttons.MinimizeButton import MinimizeButton
from src.buttons.CloseButton import CloseButton

from base64 import b64decode as b

class Launcher(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        print('Launcher GUI initialized...')
        self.geometry("750x500")
        self.configure(bg='blue', bd=0, highlightthickness=0, relief='flat', borderwidth=0)
        self.title("Toontown Online")
        self.resizable(False, False)
        self.wm_attributes('-transparentcolor', 'darkgray')

        # make fullscreen
        self.iconify()
        self.overrideredirect(True)

        

        # set the window icon
        self.iconbitmap('icon.ico')

        self.last_x = 0
        self.last_y = 0

        # This is the function that gets the position of the mouse when you click

        self.bind('<Button-1>', self.last_click_pos)
        self.bind('<B1-Motion>', self.drag_window)

        # I used a label to display the background image
        # but technically you can use a canvas, a frame, or a photoimage.
        # I used a label because it just worked out when I was testing it.

        self.background = ImageTk.PhotoImage(data=b(Background.BG))
        self.canvas = Canvas(self, width = 750, height = 500, bd = 0, highlightthickness = 0)
        self.canvas.pack()
        self.canvas.config(bg='darkgray')
        self.normalbg = self.canvas.create_image(0, 0, image = self.background, anchor = "nw")

        #### LABELS ####
        font_size = int(8)
        self.status_label = self.canvas.create_text(538, 155, anchor = "nw")
        self.canvas.itemconfig(self.status_label, text="LOG IN")
        self.version_label = self.canvas.create_text(715, 435, anchor = "center", justify="right")
        self.canvas.itemconfig(self.version_label, fill='yellow', text=
        "V1.0.1.47\nsv1.0.47.38", font=("Consolas", 8))
        self.login_prompt = Label(self.canvas, text="")
        self.login_prompt_img = ImageTk.PhotoImage(data=b(Background.LIPROMPT))
        self.login_prompt.config(image = self.login_prompt_img)
        self.user_input = Text(self.canvas, height=1, font=("Consolas", font_size), bd=2)
        self.pass_input = Text(self.canvas, height=1, font=("Consolas", font_size), bd=2)

        #### BUTTONS ####
        print("Loading buttons...")
        self.close_btn = CloseButton(self.canvas)
        self.minimize_btn = MinimizeButton(self.canvas)
        self.manage_acct_lnk = ManageAccountLink(self.canvas)
        self.forgot_pass_lnk = ForgotPasswordLink(self.canvas)
        self.create_acct_lnk = CreateAccountLink(self.canvas)
        self.play_btn = PlayButton(self.canvas)
        self.report_bug_btn = ReportABugButton(self.canvas)
        self.players_guide_btn = PlayersGuideButton(self.canvas)
        self.homepage_btn = HomepageButton(self.canvas)
        self.top_toons_btn = TopToonsButton(self.canvas)
        self.graphics_opt_btn = GraphicOptionsButton(self.canvas)
        self.quit_butn = QuitButton(self.canvas)

        ## GAME NEWS ##
        print("Loading game news...")
        self.game_news = tkinterweb.HtmlFrame(self, messages_enabled=False)

        # I used the Sunrise Game News URL to keep it consistent with the Disney launcher
        # but you can use any URL you want.
        self.game_news.load_website("https://download.sunrise.games/launcher/getNews.php?serverType=1")

        print("Placing widgets...")
        self.place_widgets()

    def place_widgets(self):
        self.login_prompt.place(x=400, y=168, height=52, width=98)
        self.user_input.place(x=499, y=175, height=19, width=140)
        self.pass_input.place(x=499, y=198, height=19, width=140)
        self.game_news.place(x=35, y=75, height=350, width=315)

    ''' 
    This is the code for the window draggability
    
    This is written to ensure that the window can be dragged around
    just like the Disney launcher.
    '''

    def drag_check(self, event):
        if event.widget in [
            self.close_btn, self.minimize_btn,
            self.manage_acct_lnk, self.forgot_pass_lnk,
            self.create_acct_lnk, self.play_btn,
            self.report_bug_btn, self.players_guide_btn,
            self.homepage_btn, self.top_toons_btn,
            self.graphics_opt_btn, self.quit_butn,
            self.user_input, self.pass_input]:
            return False
        
        # check if the mouse is over a child of the game news frame.
        for child in self.game_news.winfo_children():
            # each child of the game news frame is it's own widget
            # from my understanding, so we have to check if the event
            # widget is a child of the game news frame.
            if event.widget == child:
                return False
        return True

    def last_click_pos(self, event):
        # store the last mouse position
        self.last_x = event.x
        self.last_y = event.y

    def drag_window(self, event):
        # check if the mouse is over a widget
        if self.drag_check(event):
            pass
        else:
            return

        # get the mouse position
        x, y = event.x - self.last_x + self.winfo_x(), event.y - self.last_y + self.winfo_y()

        # set the window position to the mouse position
        self.geometry("+%s+%s" % (x , y))