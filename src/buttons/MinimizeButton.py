UP = b'/9j/4AAQSkZJRgABAgAAZABkAAD/7AARRHVja3kAAQAEAAAAUAAA/+4ADkFkb2JlAGTAAAAAAf/bAIQAAgICAgICAgICAgMCAgIDBAMCAgMEBQQEBAQEBQYFBQUFBQUGBgcHCAcHBgkJCgoJCQwMDAwMDAwMDAwMDAwMDAEDAwMFBAUJBgYJDQsJCw0PDg4ODg8PDAwMDAwPDwwMDAwMDA8MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwM/8AAEQgAEwATAwERAAIRAQMRAf/EAI4AAQEBAAAAAAAAAAAAAAAAAAgFBwEAAgMBAAAAAAAAAAAAAAAABgcCBAUDEAAABAQEAgYLAAAAAAAAAAABEQIDEhMEBQAUFQYhBzFRIjIjFkFhcbFyojNDY7NFEQAAAwUEBwYHAAAAAAAAAAABEgMAEUECBCExcQZhgaHBghMF8FGRokMWIjJCYjMUFf/aAAwDAQACEQMRAD8AVmyuXO36pqnulZa2L5cbs25VWe23BSk0NLQNrlBVVKWu06p5Ry0GAEBj6cLfNuaRFedJKYQTlEQCD3WPF2wG2svZZTQTCdT4phiIXaA3i17d3Lzbara65eLDYLfSdlGubcol2t+jUsQShxbAuvoeQkRCIxAS4lgFp8y1CCgTJTW90BxBiaq6HTVcgyKS3+OoYMVfJdymSs8xM13Q4SHvS5s/p7kPEsMT3fKQxPSPxGIXfgy69lCcpvVLwFO/GGLJja+9bdt9m1BdBUxkLJSWC5IhNTK7at0WHBSBjA8h4Ri6wA8K/qtOqK0wDcIvDAWZfR6tOqppFJBhboGINE5qc49rq23W2y21qax64tiwoW+IAlfBRD1l0evFah6fOpO2mMxbRY65/cZ5nJPzS12GEerLF7ZfEsGH6QFd9rtr2E/7iHM+YHc0vkv8bHts/M/JwNTtKilDJlZvPHxP6PZl/HwPEloXa2GMqGNMXmcJS6zRwtY7bZ0/zLSTNCnzwla/n4ji+3L8Iy6I/fiwjdBinrJ+RN+VzvpLtji5mH4Bfye7+YoD/T8x472ebT23sprNrf/Z'
DOWN = b'/9j/4AAQSkZJRgABAgAAZABkAAD/7AARRHVja3kAAQAEAAAAUAAA/+4ADkFkb2JlAGTAAAAAAf/bAIQAAgICAgICAgICAgMCAgIDBAMCAgMEBQQEBAQEBQYFBQUFBQUGBgcHCAcHBgkJCgoJCQwMDAwMDAwMDAwMDAwMDAEDAwMFBAUJBgYJDQsJCw0PDg4ODg8PDAwMDAwPDwwMDAwMDA8MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwM/8AAEQgAEwATAwERAAIRAQMRAf/EAJAAAQADAAAAAAAAAAAAAAAAAAgFBgcBAAIDAQAAAAAAAAAAAAAAAAYHAgMFBBAAAAUCBAMECwEAAAAAAAAAARECAwQTBQASFAYhFQcxIjIjQVFxsXKiM0NjsxZFEQAABAIGBgcJAAAAAAAAAAABERIDAAIhMUFxBAZhgaHBEwWR0SKCokMW8FGxMkJiMxQV/9oADAMBAAIRAxEAPwBWbK6c7flNR7pMtbF8uN2bclWe23BSkwYsBtdIJUlLXedU8o6aDACAx9OFvm3NIi/O01MINyiIBYZUGJbAjay9llthsJ3O1MNohVoDeMT27unm21W11y8WGwW+J3Uc825CXa34aliCUOLYF19DyEiIZjEBLiWAXD5lxDDgTNTU+6wbwgmxXI8Ni5Bkclr6dQ2QVf4u5VKWuYqc95HlIfFTq1+3wZeJYYnq+VCkeUvvKQnfdC69FCtKvNT3ErO+y+EHbL1txqJZI+6ESQZtNoiWWcwzJkxlMu21TwR3VaR1tYodbfETMjI8LLmLbsr8wkYGYHaAwyuUYtvFYWSeQawp0DaEVvqBvvpvaLLMa24lyRcZzDkVDq7hcJaEIfQLbhNyJLrQqyqEEmkRSJKSSgAQhhWHHpiSGo+sY0R7NIj8OqMT1+4z1Oifqlz3LlH1aYvbT4lgn/SBJfaW04Fv7jHE+YC4qfBX00HGz9T9HkarcqzUho0tXrj4n9Hu0/j4HiT1lWuBjKilTJ4ndSnWq26mDttnl/8ASxKnIq9cKXP9fmPN9un5Rl2Z/fjoZqsgp5yvgTflIvpTttvKGH5Bf5Ph/MWQ/wBPzHi+jxafbfCmo2x//9k='
HOVER = DOWN

from tkinter import *
from PIL import ImageTk
from base64 import b64decode as b

class MinimizeButton(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        self.place(x=683, y=1, height=19, width=19)

        self.config(highlightthickness=0, bd=0, relief='flat', bg="darkgray")
        self.image = ImageTk.PhotoImage(data=b(UP))
        self.btn = self.create_image(0, 0, image=self.image, anchor=NW)
        self.bind('<Leave>', self.on_leave)
        self.bind('<Enter>', self.on_enter)
        self.bind('<ButtonRelease-1>', self.on_release)
        self.bind('<ButtonPress-1>', self.on_click)
    
    def update_image(self, image):
        self.image = ImageTk.PhotoImage(data=b(image))
        self.itemconfig(self.btn, image=self.image)

    def on_enter(self, e):
        self.update_image(HOVER)

    def on_leave(self, e):
        self.update_image(UP)
    
    def on_click(self, e):
        self.update_image(DOWN)
        print("clicked")
    
    def on_release(self, e):
        self.update_image(UP)