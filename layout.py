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

        self.rwidth=self.winfo_screenwidth()
        self.rheight=self.winfo_screenheight()
        
        #top and main
        self.main_root_frame=Frame(self,bg='green')
        self.top_root_frame=Frame(self,bg='white')
        
        #side and center in main
        self.side_frame=Frame(self.main_root_frame, bg = 'yellow')
        self.center_frame=Frame(self.main_root_frame, bg = 'pink')
        
        #top and main placing
        self.top_root_frame.place(x=10,y=0,width=self.rwidth-20,height=50,anchor='nw')
        self.main_root_frame.place(x=10,y=50,width=self.rwidth-20,height=self.rheight-85,anchor='nw')
        
        #side and center placing in main
        self.side_frame.grid(row=0, column=0, sticky='nsew')
        self.center_frame.grid(row=0, column=1, sticky='nsew')
        
        self.main_root_frame.grid_columnconfigure(0, weight=1)
        self.main_root_frame.grid_columnconfigure(1, weight=4)
        self.main_root_frame.grid_rowconfigure(0, weight=1)
        self.main_root_frame.grid_rowconfigure(0, weight=1)
        
        self.update()
        
        self.top_root_width = self.top_root_frame.winfo_width()
        self.top_root_height = self.top_root_frame.winfo_height()
        
        self.side_frame_width = self.side_frame.winfo_width()
        self.side_frame_height = self.side_frame.winfo_height()
        
        self.center_frame_width = self.center_frame.winfo_width()
        self.center_frame_height = self.center_frame.winfo_height()


class main_layout(basic_layout):
    def __init__(self):
        super().__init__()
        
        self.top_root_width = self.top_root_frame.winfo_screenwidth()
        self.top_root_height = self.top_root_frame.winfo_screenheight()
        
        self.top_overlay_frame=Frame(self.top_root_frame, bg='black', width=self.top_root_width, height=self.top_root_height)
        self.side_overlay_frame=Frame(self.side_frame, bg='white', width=self.side_frame_width, height=self.side_frame_height)
        self.center_overlay_frame=Frame(self.center_frame, bg='grey', width=self.center_frame_width, height=self.center_frame_height)
                
        self.side_overlay_frame.place(x=0,y=0)
        self.top_overlay_frame.place(x=0,y=0)
        self.center_overlay_frame.place(x=0,y=0)
        
        self.update()
        
        self.top_overlay_width = self.top_overlay_frame.winfo_width()
        self.top_overlay_height = self.top_overlay_frame.winfo_height()
        
        self.side_overlay_width = self.side_overlay_frame.winfo_width()
        self.side_overlay_height = self.side_overlay_frame.winfo_height()
        
        self.center_overlay_width = self.center_overlay_frame.winfo_width()
        self.center_overlay_height = self.center_overlay_frame.winfo_height()