from tkinter import *
import tkinter as tk
import doctors_page

from PIL import Image, ImageTk

global width
global height

class basic_layout(tk.Tk):
    def __init__(self):
        super().__init__()
        self.state('zoomed')
        self.resizable(0,0)

        self.swidth=self.winfo_screenwidth()
        self.sheight=self.winfo_screenheight()
        
        
        width=self.winfo_screenwidth()
        height=self.winfo_screenheight()
        
        #top and main
        self.main_root_frame=Frame(self,bg='green')
        self.top_root_frame=Frame(self,bg='white')
        
        #side and center in main
        self.side_frame=Frame(self.main_root_frame, bg = 'yellow',width=10, height=100)
        self.center_frame=Frame(self.main_root_frame, bg = 'pink',width=10, height=100)
        
        #top and main placing
        self.top_root_frame.place(x=10,y=0,width=self.swidth-20,height=50,anchor='nw')
        self.main_root_frame.place(x=10,y=50,width=self.swidth-20,height=self.sheight-85,anchor='nw')
        
        #side and center placing in main
        self.side_frame.grid(row=0, column=0, sticky='nsew')
        self.center_frame.grid(row=0, column=1, sticky='nsew')
        
        
        self.main_root_frame.grid_columnconfigure(0, weight=1)
        self.main_root_frame.grid_columnconfigure(1, weight=4)
        self.main_root_frame.grid_rowconfigure(0, weight=1)
        self.main_root_frame.grid_rowconfigure(0, weight=1)


class main_layout(basic_layout):
    def __init__(self):
        super().__init__()
        self.top_overlay_frame=Frame(self.top_root_frame, bg='black')
        self.side_overlay_frame=Frame(self.side_frame, bg='white')
        self.center_overlay_frame=Frame(self.center_frame, bg='grey')
                
        self.side_overlay_frame.pack(fill=BOTH, expand="True")
        
        #prevent 
        #self.side_overlay_frame.pack_propagate(False)
        
        self.top_overlay_frame.pack(fill=BOTH, expand="True")
        self.center_overlay_frame.pack(fill=BOTH, expand="True")
