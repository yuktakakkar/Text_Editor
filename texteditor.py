import tkinter
import os
from tkinter import *
from tkinter import filedialog, Menu, END, messagebox, simpledialog
import tkinter.scrolledtext as ScrolledText

tk = tkinter.Tk()
text = ScrolledText.ScrolledText(tk, width = 500, height = 80)
text.pack()

tk.title("Write your text here")

def new():
    if(len(text.get('1.0', END+'-1c')) > 0):
        if messagebox.askyesno('Save','Do you want to save?'):
            save()
        else:
            text.delete('1.0', END)
    tk.title("Write your text here")

def open():
    file = filedialog.askopenfile(parent = tk, mode = 'rb', )
    tk.title(os.path.basename(file.name))

    if file != None:
        read_it = file.read()
        text.insert('1.0', read_it)
        file.close()

def save():
    file = filedialog.asksaveasfile(mode = "w")

    if file != None:
        data = text.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def exit():
    if messagebox.askyesno("This is your exit box", "Are you sure you want to exit?"):
        tk.destroy()

def find():
    found = simpledialog.askstring("Find", "What do you want to find")
    text1 = text.get('1.0', END+'-1c')
    occurance = text1.upper().count(found.upper())
    if text1.upper().count(found.upper()):
        lbl111 = messagebox.showinfo("Found!", found + " has " + str(occurance) + " occurances")
    else:
        lbl222 = messagebox.showinfo("Not Found!", "Match Not Found!")

def help():
    lbl3333 = messagebox.showinfo("About", "This is a text editor made in python. You can do certain things on this text editor.")

def undo():
    text.edit_undo()

    #create a toplevel menu
menu = Menu(tk)

#display the menu
tk.config(menu=menu)

#create pull down menu
filemenu = Menu(tk)

menu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "New", command = new)
filemenu.add_command(label = "Open", command = open)
filemenu.add_command(label = "Save As", command = save)
filemenu.add_command(label = "Find", command = find)
filemenu.add_command(label = "Exit", command = exit)

editmenu = Menu(menu)
menu.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Undo", command = undo)
editmenu.add_command(label = "Cut", command=lambda: text.event_generate("<<Cut>>"))
editmenu.add_command(label = "Copy", command=lambda: text.event_generate("<<Copy>>"))
editmenu.add_command(label = "Paste", command=lambda: text.event_generate("<<Paste>>"))

helpmenu = Menu(menu)
menu.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "About text editor", command = help)

tk.mainloop()