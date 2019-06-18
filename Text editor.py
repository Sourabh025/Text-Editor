import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

from tkinter.messagebox import showinfo

def newfile():
    global file
    TextArea.delete(1.0, END)
    root.title("Untitled -Notepad")


def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")],title="Select file ")
    if file =="":
        file=None

    else:
        TextArea.delete(1.0, END)
        root.title(os.path.basename(file) + "-Notepad")
        f=open(file,"r")
        TextArea.insert(1.0 , f.read())

        f.close()


def save():
    global file
    if file == None:
        file = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")], title="Select destination ")

        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0, END))

    else:

        f=open(file,"W")
        f.write(TextArea(1.0,END))
        f.close()



def exit():
    root.destroy()

def a():
    s=tkinter.messagebox.showinfo(message='Coded by ~Sourabh',title="About")
    s.pack()

def v():
    s=tkinter.messagebox.showinfo(message='Current verion is 1.0 Copyright @2019',title="Version")
    s.pack(width=50)

def cut():
    TextArea.event.genrate(("<<Cut>>"))

def copy():
    TextArea.event.genrate(("<<Copy>>"))

def paste():
    TextArea.event.genrate(("<<Paste>>"))





if __name__ == '__main__':
    root=Tk()
    root.title("Text Editor")
    root.geometry("700x500")
    menubar=Menu(root)
    global file
    file=None
    root.config(menu=menubar)
    m1=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File", menu=m1)

    m1.add_command(label="Newfile",command=newfile)
    m1.add_command(label="Save",command=save)

    m1.add_command(label="Open",command=openfile)

    m2=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit", menu=m2)

    m2.add_command(label="Copy",command= copy)
    m2.add_command(label="Paste",command=paste)
    m2.add_command(label="Cut",command=cut)

    m3 = Menu(menubar,tearoff=0)

    m3.add_command(label="About",command=a)
    m3.add_command(label="Version",command=v)
    menubar.add_cascade(label="Other", menu=m3)

    m1.add_command(label="Exit",command=exit)



    TextArea=Text(root, font="lucida 13")
    TextArea.pack(expand =TRUE , fill=BOTH)

    root.config(menu=menubar)

    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    #popup right click menu


    root.mainloop()

