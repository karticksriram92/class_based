from tkinter import *
from tkinter import ttk
import layout, main_page
from layout import *

print("hello")

#specifying frame as super class makes it only initialize ttk.Frame rather than root so it didnt made another window just made an overlay
#seems like a hollow class with base class of frame and passing self as self so still self till root is accessible but not initiated.(should dig in more).
class show_top_frame(ttk.Frame):

    def __init__(self, container,frame):
        #passing root/main_frame as container to Frame __init__ by using super()
        super().__init__(container)
        self.container=container
        self.frame=frame
        
        lb=Label(self.frame, bg='red')
        lb.grid(column=0,row=0)
        
class show_side_frame(ttk.Frame):

    def __init__(self, container,frame):
        #passing root/main_frame as container to Frame __init__ by using super()
        super().__init__(container)
        self.container=container
        self.frame=frame
        main_page.main_page_display.show_img(self.frame)

class show_center_frame(ttk.Frame):

    def __init__(self, container,frame):
        #passing root/main_frame as container to Frame __init__ by using super()
        super().__init__(container)
        self.container=container
        self.frame=frame
        
        lb=Label(self.frame, bg='red')
        lb.grid(column=0,row=0)