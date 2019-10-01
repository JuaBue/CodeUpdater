# coding: utf-8
from Tkinter import *
import tkMessageBox
from Tkconstants import *
import Tkinter as tk     # python 2
import tkFont as tkfont  # python 2
import os.path
from tkFileDialog import *


class Menu(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.expaded = 0
        self.folder_path = "C:\Users\juan.bueno\Desktop\INGENICO"
        parent.geometry("675x100+386+371")
        parent.resizable(width=False, height=False)
        parent.iconbitmap(default='logos\cu_icon.ico')
        self.parent.title("CodeUpdater")
        Menu.configura(self, parent)

    def configura(self, parent):
        self.Labelframe1 = LabelFrame(parent)
        self.Labelframe1.place(relx=0.02, y=6, height=75, width=540)
        self.Labelframe1.configure(text="Ubicación Paquete SW", borderwidth="2", relief=GROOVE, width=435)

        self.Labelframe2 = LabelFrame(parent)
        self.Labelframe2.configure(relief=FLAT)
        self.Labelframe2.place(relx=0.82, y=0.5, height=100, width=120)

        uploadimage = PhotoImage(file="logos\\uparrow.gif")
        self.Button1 = Button(self.Labelframe2)
        self.Button1.place(x=5, y=0, height=30, width=101)
        self.Button1.configure(image=uploadimage, compound="right", text="CARGAR ", relief=FLAT, anchor="e", font='Helvetica 9 bold', command=lambda:None)

        exitimage = PhotoImage(file="logos\\error.gif")
        self.Button2 = Button(self.Labelframe2)
        self.Button2.place(x=5, y=30, height=30, width=101)
        self.Button2.configure(image=exitimage, compound="right", text="SALIR ", relief=FLAT, anchor="e", font='Helvetica 9 bold', command=lambda:self.cerrarapp())\

        moreimage = PhotoImage(file="logos\\plus.gif")
        self.Button3 = Button(self.Labelframe2)
        self.Button3.place(x=5, y=60, height=30, width=101)
        self.Button3.configure(image=moreimage, compound="right", text="PLATFORM ", relief=FLAT,  anchor="e",  font='Helvetica 9 bold', command=lambda:self.expandir(parent))

        image = PhotoImage(file="logos\\folder.gif")
        self.Button4 = Button(self.Labelframe1)
        self.Button4.place(relx=0.90, rely=0.2, height=20, width=20)
        self.Button4.configure(image=image, width="20", height="20", relief=GROOVE, bd=0, command=lambda: self.selectpath())

        self.Entry4 = Entry(self.Labelframe1)
        self.Entry4.place(relx=0.03, rely=0.20, height=19, width=430)
        self.Entry4.insert(INSERT, self.folder_path)

        self.Labelframe3 = LabelFrame(parent)
        self.Labelframe3.place(relx=0.02, y=100, height=60, width=540)
        self.Labelframe3.configure(text="Ubicación Paquete Paltaformado", borderwidth="2", relief=GROOVE, width=435)

        self.Entry5 = Entry(self.Labelframe3)
        self.Entry5.place(relx=0.03, rely=0.20, height=19, width=430)
        self.Entry5.insert(INSERT, "aqa")

        image2 = PhotoImage(file="logos\\folder.gif")
        self.Button5 = Button(parent)
        self.Button5.place(x=500, y=122, height=20, width=20)
        self.Button5.configure(image=image2, width="20", height="20", relief=FLAT, command=lambda: self.selectpath())

        parent.mainloop()

    def selectpath(self):
        filename = askopenfilename()
        if os.path.isfile(filename):
            self.folder_path = filename
            self.Entry4.delete(0, "end")
            self.Entry4.insert(END, self.folder_path)
        else:
            result = tkMessageBox.showerror("CodeUpdater", "El fichero seleccionado no es valido", icon='error')
            if result == 'yes':
                tk.destroy()
            else:
                pass

    def cerrarapp(self):
        result = tkMessageBox.askquestion("CodeUpdater", "¿Desea salir de la aplicación?", icon='warning')
        if result == 'yes':
            tk.destroy()
        else:
            pass

    def noselectapp(self):
        result = tkMessageBox.showerror("CodeUpdater", "No ha seleccionado el fichero a cargar", icon='error')
        if result == 'yes':
            tk.destroy()
        else:
            pass

    def expandir(self, parent):
        if self.expaded == 0:
            parent.geometry("675x180+386+371")
            self.expaded = 1

        else:
            parent.geometry("675x100+386+371")
            self.expaded = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        tk = Tk()
        Menu(parent=tk)
    else:
        filepath = sys.argv[1]
        print filepath
        pass

