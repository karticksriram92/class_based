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
        self.top_mainpage_frame=Frame(self.top_overlay_frame, bg='black')
        self.side_mainpage_frame=Frame(self.side_overlay_frame, bg='white', borderwidth=4, relief='ridge')
        self.center_mainpage_frame=Frame(self.center_overlay_frame, bg='white', relief='groove')
        
        #self.side_mainpage_frame.pack(fill=BOTH, expand="True")
        self.side_mainpage_frame.pack(fill=BOTH, expand="True")
        
        #prevent child to change parent size
        self.side_mainpage_frame.pack_propagate(False)
        
        self.top_mainpage_frame.pack(fill=BOTH, expand="True")
        self.center_mainpage_frame.pack(fill=BOTH, expand="True")
        
        self.update()
        
        self.side_swidth=self.side_mainpage_frame.winfo_width()
        self.side_sheight=self.side_mainpage_frame.winfo_height()
        #print(self.side_swidth)
        #print(self.side_sheight)
        
        
class main_page_display(main_page_layout):
    def __init__(self):
        #it will call parent class again so it will make another window, so either call this class at bottom(can use super() then) or dont call super()
        super().__init__()
        #self.show_img()
        # button= Button(self.center_mainpage_frame , command=self.change_page)
        # button.pack()
        
        display_image(self.side_mainpage_frame,self.swidth, self.sheight)
        
        front_frame=Frame(self.center_mainpage_frame,bg='red')
        lb_admin = Label(self.center_mainpage_frame, width=200, height=200)
        lb_doctor = Label(self.center_mainpage_frame, width=200, height=200)
        lb_receptionist = Label(self.center_mainpage_frame, width=200, height=200)
        
        front_frame.place(x=0,y=0,width=self.swidth-20,height=self.sheight-85,anchor='nw')
        
    # def get_img(self):
        # img_file=Image.open("C:/Users/kartick/Downloads/test.png")
        # size_fit=(int((self.swidth/4)-8), int(self.sheight-93))
        # resized_img_file=img_file.resize(size_fit ,Image.ANTIALIAS)
        # self.img=ImageTk.PhotoImage(resized_img_file)
        # return self.img
    
    # def show_img(self):
        # img = self.get_img()
        # label=Label(self.side_mainpage_frame,image=self.img)
        # label.pack(fill=BOTH, expand="True")
    
    def change_page(self):
        for widgets in self.center_mainpage_frame.winfo_children():
            widgets.destroy()
        for widgets in self.side_mainpage_frame.winfo_children():
            widgets.destroy()
        doctors_page.show_top_frame(self,self.top_mainpage_frame, self.swidth, self.sheight)
        doctors_page.show_side_frame(self,self.side_mainpage_frame, self.swidth, self.sheight)
        doctors_page.show_center_frame(self,self.center_mainpage_frame, self.swidth, self.sheight)
        
        
    def run(self):
        self.mainloop()
        
        
class display_image(ttk.Label):
    def __init__(self, container, swidth, sheight):
        #this is important using super() otherwise show_img wont work
        super().__init__()
        self.swidth = swidth
        self.sheight = sheight
        #print(self.sheight)
        self.show_img(container)
    
    def get_img(self):
        img_file=Image.open("C:/Users/kartick/Downloads/test.png")
        size_fit=(int((self.swidth/4)-8), int(self.sheight-93))
        resized_img_file=img_file.resize(size_fit ,Image.ANTIALIAS)
        self.img=ImageTk.PhotoImage(resized_img_file)
        #print(self.img)
        return self.img
    
    #def show_img(self):
    def show_img(self, container):
        print(container)
        img = self.get_img()
        #img = self.get_img()
        #print(img)
        print(self.img)
        #label=Label(self.side_mainpage_frame,image=self.img)
        label=Label(container,image=self.img)
        #label=Label(container,text="hello world", bg='red')
        # button= Button(self.center_mainpage_frame , command=self.change_page)
        # button.pack()
        label.pack(fill=BOTH, expand="True")

if __name__ == "__main__":
    #this should be the entry of this program.
    app = main_page_display()
    app.run()
