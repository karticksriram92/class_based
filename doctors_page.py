from tkinter import *
from tkinter import ttk
import layout, main_page
from layout import *

print("hello")

#specifying frame as super class makes it only initialize ttk.Frame rather than root so it didnt made another window just made an overlay
#seems like a hollow class with base class of frame and passing self as self so still self till root is accessible but not initiated.(should dig in more).
class show_top_frame(ttk.Frame):

    def __init__(self, container,frame, rwidth, rheight):
        #passing root/main_frame as container to Frame __init__ by using super()
        super().__init__(container)
        self.container=container
        self.frame=frame
        
        # self.side_width=self.frame.winfo_width()
        # print(self.side_width)
        
        self.rwidth=rwidth
        self.rheight=rheight
        
        # lb=Label(self.frame, bg='red')
        # lb.grid(column=0,row=0)
        
class show_side_frame(ttk.Frame):

    def __init__(self, container,frame, rwidth, rheight,side_width, side_height):
        #passing root/main_frame as container to Frame __init__ by using super()
        super().__init__(container)
        self.container=container
        self.frame=frame
        self.rwidth=rwidth
        self.rheight=rheight
        self.side_width= side_width
        self.side_height=side_height
        main_page.display_image(self.frame, self.side_width, self.side_height, "C:/Users/91807/Downloads/kona/project/res/doctor.jpg")

class show_center_frame(ttk.Frame):

    def __init__(self, container,frame, rwidth, rheight):
        #passing root/main_frame as container to Frame __init__ by using super()
        super().__init__(container)
        self.container=container
        self.frame=frame
        self.rwidth=rwidth
        self.rheight=rheight
        
        self.frame.configure(bg='red')
        lb=Label(self.frame, bg='red')
        lb.grid(column=0,row=0)