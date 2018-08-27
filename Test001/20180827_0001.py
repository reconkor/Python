import tkinter as tk
#from tkinter import ttk
win = tk.Tk()
win.title("Python GUI")

a_label = tk.Label(win, text="Enter Name")
a_label.grid(column=0, row=0)

def click_me():
    action.configure(text="I have been clicked")
    a_label.configure(foreground="red")
#    a_label.configure(text="A Red label")
    a_label.configure(text="Hello " + name.get())

name = tk.StringVar()
name_entered = tk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

action = tk.Button(win, text="click me", command=click_me)
action.grid(column=1, row=0)
win.mainloop()
