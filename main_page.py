from tkinter import *
import tkinter as tk
from tkinter import ttk
import doctors_page
import layout

from PIL import Image, ImageTk

from threading import Timer

class main_page_layout(layout.main_layout):
    def __init__(self):
        super().__init__()
        self.top_mainpage_frame=Frame(self.top_overlay_frame, bg='black', width = self.top_overlay_width, height = self.top_overlay_height)
        self.side_mainpage_frame=Frame(self.side_overlay_frame, bg='white', width = self.side_overlay_width, height = self.side_overlay_height)
        self.center_mainpage_frame=Frame(self.center_overlay_frame, bg='white', width = self.center_overlay_width, height = self.center_overlay_height)
        
        self.top_mainpage_frame.place(x=0,y=0)
        self.side_mainpage_frame.place(x=0,y=0)
        self.center_mainpage_frame.place(x=0,y=0)
        
        self.update()
        
        self.side_width=self.side_mainpage_frame.winfo_width()
        self.side_height=self.side_mainpage_frame.winfo_height()
        
        self.top_width=self.top_mainpage_frame.winfo_width()
        self.top_height=self.top_mainpage_frame.winfo_height()
        
        self.center_width=self.center_mainpage_frame.winfo_width()
        self.center_height=self.center_mainpage_frame.winfo_height()
        
        
class main_page_display(main_page_layout):
    def __init__(self):
        #it will call parent class again so it will make another window, so either call this class at bottom(can use super() then) or dont call super()
        super().__init__()
        
        display_image(self.side_mainpage_frame,self.side_width, self.side_height, "C:/Users/91807/Downloads/kona/project/res/admin.jpg")
        
        self.front_frame=Frame(self.center_mainpage_frame,bg='grey')
        self.lb_admin = Frame(self.front_frame, bg='yellow')
        self.lb_doctor = Frame(self.front_frame, bg="red")
        self.lb_receptionist = Frame(self.front_frame, bg="blue")
        
        self.front_frame.place(x=0,y=0,width=self.center_width,height=self.center_height,anchor='nw')
        self.front_frame.columnconfigure(0,weight=1)
        self.front_frame.columnconfigure(1,weight=1)
        self.front_frame.columnconfigure(2,weight=1)
        self.front_frame.columnconfigure(3,weight=1)
        self.front_frame.columnconfigure(4,weight=1)
        self.front_frame.columnconfigure(5,weight=1)
        self.front_frame.columnconfigure(6,weight=1)
        self.front_frame.columnconfigure(7,weight=1)
        self.front_frame.columnconfigure(8,weight=1)
        self.front_frame.columnconfigure(9,weight=1)
        
        self.front_frame.rowconfigure(0,weight=1)
        self.front_frame.rowconfigure(1,weight=1)
        self.front_frame.rowconfigure(2,weight=1)
        self.front_frame.rowconfigure(3,weight=1)
        self.front_frame.rowconfigure(4,weight=1)
        self.front_frame.rowconfigure(5,weight=1)
        self.front_frame.rowconfigure(6,weight=1)
        self.front_frame.rowconfigure(7,weight=1)
        self.front_frame.rowconfigure(8,weight=1)
        
        self.lb_admin.grid(column=1,row=3, columnspan=2, rowspan=2, sticky=NSEW)
        self.lb_doctor.grid(column=4,row=3, columnspan=2, rowspan=2, sticky=NSEW)
        self.lb_receptionist.grid(column=7,row=3, columnspan=2, rowspan=2, sticky=NSEW)
        
        self.update()
        
        self.admin_width = self.lb_admin.winfo_width()
        self.admin_height = self.lb_admin.winfo_height()
        
        display_image(self.lb_admin, self.admin_width, self.admin_height, "C:/Users/91807/Downloads/kona/project/res/adm.jpg")
        display_image(self.lb_doctor, self.admin_width, self.admin_height, "C:/Users/91807/Downloads/kona/project/res/doc.jpg", self.change_page)
        display_image(self.lb_receptionist, self.admin_width, self.admin_height, "C:/Users/91807/Downloads/kona/project/res/recep.jpg")
    
    def change_page(self):
        for widgets in self.center_mainpage_frame.winfo_children():
            widgets.destroy()
        for widgets in self.side_mainpage_frame.winfo_children():
            widgets.destroy()
        doctors_page.show_top_frame(self,self.top_mainpage_frame, self.rwidth, self.rheight)
        doctors_page.show_side_frame(self,self.side_mainpage_frame, self.rwidth, self.rheight, self.side_width,self.side_height)
        doctors_page.show_center_frame(self,self.center_mainpage_frame, self.rwidth, self.rheight)
        
        
    def run(self):
        self.mainloop()
        
        
class display_image(ttk.Button):
    def __init__(self, container, side_width, side_height, url, command=""):
        #this is important using super() otherwise show_img wont work
        super().__init__()
        self.side_width = side_width
        self.side_height = side_height
        self.url = url
        self.command=command
        self.show_img(container)
    
    def get_img(self):
        img_file=Image.open(self.url)
        #size_fit=(int((self.rwidth/4)-8), int(self.rheight-93))
        size_fit=(self.side_width, self.side_height)
        resized_img_file=img_file.resize(size_fit ,Image.ANTIALIAS)
        self.img=ImageTk.PhotoImage(resized_img_file)
        return self.img
    
    #def show_img(self):
    def show_img(self, container):
        img = self.get_img()
        # print(self.side_width)
        btn=Button(container,image=self.img, width=self.side_width, height=self.side_height, command=self.command)
        btn.place(x=0,y=0)

if __name__ == "__main__":
    #this should be the entry of this program.
    app = main_page_display()
    app.run()
