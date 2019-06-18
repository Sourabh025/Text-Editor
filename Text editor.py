from tkinter import *
import tkinter

root = tkinter.Tk()

w = tkinter.Label(root, text="Right-click to display menu", width=40, height=20)
w.pack()

# create a menu
popup = tkinter.Menu(root, tearoff=0)
popup.add_command(label="Next")  # , command=next) etc...
popup.add_command(label="Previous")
popup.add_separator()
popup.add_command(label="Home")


def do_popup(event):
    #display the popup menu
    popup.tk_popup(event.x_root, event.y_root, 0)



w.bind("<Button-3>", do_popup)

b = tkinter.Button(root, text="Quit", command=root.destroy)
b.pack()

root.mainloop()