'''
 This software is not affiliated with the Walt Disney Company or its affiliates.

 This is open source software, and you are welcome to modify and/or redistribute it
 under certain conditions; see the license for details.
 This software is provided "as is" and without any express or implied warranties,
 including, without limitation, the implied warranties of merchantability and fitness
 for a particular purpose.

------------------------------------------------------------------
 Project: Toontown Launcher
 Project Version: 0.0.1a
 Python Version: 3.8.10
 Start file: splash.py

 This launcher is a recreation of the Toontown Online Launcher. This launcher is
 made to be used with Toontown Private Servers that want an original feel to their
 launcher and can be modified to fit their needs.
 ------------------------------------------------------------------
'''

try:
    from tkinter import *
except ImportError:
    from Tkinter import *
from launcher import Launcher

class Splash(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        print('Splash screen initialized...')

        #TODO: Add a splash screen
        self.eval('tk::PlaceWindow . center')
        self.withdraw()
        self.geometry("511x323")

try:
    if __name__ == "__main__":
        splash = Splash()
        launcher = Launcher(splash)
        launcher.mainloop()
except Exception as e:
    if e != None:
        print(e)
        input('Press enter to exit...')
    exit()