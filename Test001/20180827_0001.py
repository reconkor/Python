import tkinter as tk
from tkinter import ttk
from tkinter import Menu

def _quit():
    win.quit()
    win.destroy()
    exit()

def click_me():
    action.configure(text="I have been clicked")
    a_label.configure(foreground="red")
#    a_label.configure(text="A Red label")
    a_label.configure(text="Hello " + name.get() + ":"+ number.get())

win = tk.Tk()
win.title("Python GUI")

a_label = tk.Label(win, text="Enter Name")
a_label.grid(column=0, row=0)

b_label = tk.Label(win, text="Choose a Number")
b_label.grid(column=1, row=0)

#Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

#Add Menu item
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)

name = tk.StringVar()
name_entered = tk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number)
number_chosen['values'] = (1, 2, 4, 42, 50)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

action = tk.Button(win, text="click me", command=click_me)
action.grid(column=2, row=1)
#action.configure(state="disabled")

#name_entered.focus()

#======================
# Start GUI
#======================
win.mainloop()
