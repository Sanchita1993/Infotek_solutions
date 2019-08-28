
# coding: utf-8

# In[ ]:



# import tkinter library for GUI
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile


def NewFile():
    print("New File!")
    
def OpenFile():
    filename = tkinter.filedialog.askopenfilename(parent=root)
    f = open(filename)
    # to print the content of file.
    for line in f:
        print(line)

def Save():
    f = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close()

    
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Save", command=asksaveasfile)
filemenu.add_command(label="Exit", command=root.quit)
# mainloop() is an infinite loop used to run the application, wait for an event to 
#occur and process the event till the window is not closed.
mainloop()

