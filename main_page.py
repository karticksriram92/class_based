from tkinter import *
import tkinter as tk
import doctors_page

from threading import Timer

class basic_layout(tk.Tk):
    def __init__(self):
        super().__init__()
        self.state('zoomed')
        self.resizable(0,0)

        swidth=self.winfo_screenwidth()
        sheight=self.winfo_screenheight()

        self.main_root_frame=Frame(self,bg='green')
        self.top_root_frame=Frame(self,bg='white')

        self.top_root_frame.place(x=10,y=0,width=swidth-20,height=50,anchor='nw')
        self.main_root_frame.place(x=10,y=50,width=swidth-20,height=sheight-85,anchor='nw')


class main_layout(basic_layout):
    def __init__(self):
        super().__init__()
        
        self.top_overlay_frame=Frame(self.top_root_frame, bg='red')
        self.main_overlay_frame=Frame(self.main_root_frame, bg='blue')
        
        
        side_frame=Frame(self.main_overlay_frame, bg = 'white',width=10, height=100)
        center_frame=Frame(self.main_overlay_frame, bg = 'pink',width=10, height=100)
        
        # t=Timer(5.0, self.change_page)
        # t.start()
        
        
        self.top_overlay_frame.pack(fill=BOTH, expand="true")
        self.main_overlay_frame.pack(fill=BOTH, expand="true")
        side_frame.grid(row=0, column=0, sticky='nsew')
        center_frame.grid(row=0, column=1, sticky='nsew')
        
        self.main_overlay_frame.grid_columnconfigure(0, weight=1)
        self.main_overlay_frame.grid_columnconfigure(1, weight=4)
        self.main_overlay_frame.grid_rowconfigure(0, weight=1)
        self.main_overlay_frame.grid_rowconfigure(0, weight=1)
        

    def change_page(self):
        for widgets in self.main_root_frame.winfo_children():
            widgets.destroy()
        #doctors_page.show_frame(self,self.main_root_frame)
        
    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = main_layout()
    app.run()