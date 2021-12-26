from tkinter import *
from tkinter import ttk

class show_frame(ttk.Frame):

    def __init__(self, container,frame):
        #passing root/main_frame as container to Frame __init__ by using super()
        super().__init__(container)
        self.container=container
        self.frame=frame
        
        lb=Label(self.frame, text="test" )
        lb.grid(column=0,row=0)