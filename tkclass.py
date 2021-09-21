from tkinter import *
import tkinter.messagebox as messagebox


class GUI(Tk):
    def __init__(self,title:str,geometry:str,icon=None,background="#1c1c1c",fixed_geometry=True):
        super().__init__()
        self.width = int(geometry.split('x')[0])
        self.height = int(geometry.split('x')[1])
        self.background_color = background
        self.geometry(geometry)
        self.title(title)
        self.wm_iconbitmap(icon)
        self.configure(background=self.background_color)
        self.minsize(width=self.width,height=self.height)
        if fixed_geometry:
            self.maxsize(width=self.width,height=self.height)


    def error_box(self,title:str,message:str):
        errbox = messagebox.showerror(title=title,message=message)
        return errbox


    def info_box(self,title:str,message:str):
        infobox = messagebox.showinfo(title=title,message=message)
        return infobox


    def askyesno(self,title:str,message:str):
        askbox = messagebox.askyesno(title=title,message=message)
        return askbox


    def exit_window(self):
        exit_box = messagebox.askyesno(title="Confirm Exit",message="Are you sure you want exit?")
        if exit_box:
            self.destroy()
        else:
            return


    def run(self):
        self.mainloop()
