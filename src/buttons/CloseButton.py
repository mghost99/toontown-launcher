UP = b'/9j/4AAQSkZJRgABAgAAZABkAAD/7AARRHVja3kAAQAEAAAAUAAA/+4ADkFkb2JlAGTAAAAAAf/bAIQAAgICAgICAgICAgMCAgIDBAMCAgMEBQQEBAQEBQYFBQUFBQUGBgcHCAcHBgkJCgoJCQwMDAwMDAwMDAwMDAwMDAEDAwMFBAUJBgYJDQsJCw0PDg4ODg8PDAwMDAwPDwwMDAwMDA8MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwM/8AAEQgAEwATAwERAAIRAQMRAf/EAJQAAQADAQAAAAAAAAAAAAAAAAcFBggJAQACAwEAAAAAAAAAAAAAAAAHCAMEBQYQAAADBgQEAwkAAAAAAAAAAAECAxESEwQUBQAhFQYxQTIWI0MXUWGRwSKyUwcIEQAAAwUEBAkNAAAAAAAAAAABEQIAEgMTBCExQQVRFAYH8HGBkaEiQiMXYbHB8TJSYnKSskOjRP/aAAwDAQACEQMRAD8ADL1u6TnUamcIM6Rc6o2eynVOlLQEjilVTYIiB1hVMAw02gV0HjZ8Bxmuai+KU3AzK7ptzdPRU0OPHhpiVUVALFSweCElVoJSCgEAG55RPCJgAu3m0xuWct8ylcrZLSNiOgcBjWlE0mnmLGKy8VRNUo82588YSqicN3DjwY155u3yvMaRUDMISFoECfACiQ9CkqvsHQIcRMo+t0xR1EAj2itgPi9qNXTutayG74jep3LjiWZGueG7ov8AqwNlM8AYk+VP/tkmVmryZ8z5/wAeh7EmG90yE9srcc7t++FVSWtBQkExUDqQRMYZdYrOJVCGeAfjm3EcSGqLaGk+fDkZtth9raHMMsp62EoBSuElKi7C0XgIYXiA8QYWtSr7uKSCTURSUfMqDuXvxJSUS3zHBtbaHaamCnFCBMVWNL+n+76GPpU3U9t9y0zhmuV0Bz2PQfFd4s5NxcmQzI8Xeg/OwL8RaWe7MS7rUp4+3Je+/u3rjxJtbf1dp7tpru1noR6avr9YeaLYVDlCZ+X6XuGeK9KZ2H6Olg7uZnd9L1ojA5cqQXxzbX9EvrO+Rsdfq3S+8LVF7SqqstL3JqbjXvLheA8zpi5NZzxo1Byx9rkL1sTNtJuqxHNYddF6TLmfs65e9LtI8G6ic/J6fl9uOZZNue/hyt//2Q=='
DOWN = b'/9j/4AAQSkZJRgABAgAAZABkAAD/7AARRHVja3kAAQAEAAAAUAAA/+4ADkFkb2JlAGTAAAAAAf/bAIQAAgICAgICAgICAgMCAgIDBAMCAgMEBQQEBAQEBQYFBQUFBQUGBgcHCAcHBgkJCgoJCQwMDAwMDAwMDAwMDAwMDAEDAwMFBAUJBgYJDQsJCw0PDg4ODg8PDAwMDAwPDwwMDAwMDA8MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwM/8AAEQgAEwATAwERAAIRAQMRAf/EAJQAAAMBAQAAAAAAAAAAAAAAAAYHCAMJAQACAwEAAAAAAAAAAAAAAAAHCAIEBQYQAAADBwEGBQUBAAAAAAAAAAECAxESEwQUBQYVACExIjIWQVEjQxfBsjNTBwgRAAADBAYECQ0AAAAAAAAAAAERAjESAxMAIUFRBAVhMhQGgZGhwSJCYiMH8HGx0fFScpKyQ6NEF//aAAwDAQACEQMRAD8ARN4zGQnlpELkYh5e6LqpWeTmllELeiRMwpEmbgZFhzgucBBMoiBADmP5gOM2zRRqBACJWA0SaOnzc9GI8NfCrB5LgoeMxcIImIiJSpSlJeCElRCCUgNQCBg8onhHopqaBq3i7yFzuExIW+UxtXHRAbrNW1A0iiioYzhEF0IqiaplBby9TAE3ABEOfXiwiglQdbVC0bxC4r+ChjzrdDI81hbFjIaIyVp10JJUJhKBTQJtQhcLSFj/ADdMUdRAI9orYD4vajV07rWshu+o3qd3cdrEyMx4WcjfmsOiw/wGJPlT/wB2SZVbPJnzPj+3c9aVEzlNmm8YyeYxLIpg1rTkAC3TE+ukKrsmiJzIrJJl/JFTM0u8AaPMIb2RWClGsAMTMAMjOw9FtGl3b3qw+aZLAxODdVMhJQvsKSbwCF9Ygyw66jH7plVlRx64Y4iKoSMuspNY4s0p1hMuYhVUZt0pCqCJAaVQAaDHWCUQdjAwMVUZMYdZirqmCm6toMFraSxGMh5alaIawWmIkAESrPRxs9Venx/l9DH0qbqe2+5aZwzXK6A55PQfVd4s8G7aEyGZHa7yH6aDD+i4We7MS7tUp4+vJe+vu3mHaVK2/wBXae7aa7tZ6Eemr6/WHmi2FQ7oTP28r3DftXwpnUfNy0DvgzO76XtRGBy5Ugu3Nrful9J3RSOv5bpfeFqi9pVVWWl7k1Nxr3twvQeZ0xdzWeO2jiDljrcBe2hM30m7LEc2h10XpMuZ+Tpl70usjsp1E8fZ6fp9u3M0Tbjb5cNP/9k='
HOVER = DOWN

from tkinter import *
from PIL import ImageTk
from base64 import b64decode as b

class CloseButton(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        self.place(x=706, y=1, height=19, width=19)

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
        exit()
    
    def on_release(self, e):
        self.update_image(UP)