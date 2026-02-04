from tkinter import *
from tkinter import messagebox
import main

def login():
    if user.get() == "admin" and pwd.get() == "1234":
        win.destroy()
        main.start_app()   # THIS is the key change
    else:
        messagebox.showerror("Error", "Wrong credentials")


win = Tk()
win.title("Login")

Label(win, text="Username").grid(row=0, column=0)
user = Entry(win)
user.grid(row=0, column=1)

Label(win, text="Password").grid(row=1, column=0)
pwd = Entry(win, show="*")
pwd.grid(row=1, column=1)

Button(win, text="Login", command=login).grid(row=2, column=0, columnspan=2)

win.mainloop()
