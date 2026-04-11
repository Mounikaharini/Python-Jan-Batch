import tkinter as tk
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk
from PIL import *

a = tk.Tk()
a.geometry("1400x900")
a.config(bg="#E6E6FA")
a.title("FlickIt: Casual, fun, and tech-friendly")

def book1():
    a.destroy()
    import likform
m1 = Image.open(r"m1.jpg")
mr1 = ImageTk.PhotoImage(m1.resize((201,251)))
photo =Label(a, image=mr1)
photo.place(x=100,y=100)
b1 = Button(a, text="Book", font=("Palatino Linotype", 15), bg="FireBrick", fg="white", width=15, command=book1)
b1.place(x=100, y=400)

m2 = Image.open(r"m2.jpg")
mr2 = ImageTk.PhotoImage(m2.resize((201,251)))
photo =Label(a, image=mr2)
photo.place(x=400,y=100)
b2 = Button(a, text="Book", font=("Palatino Linotype", 15), bg="FireBrick", fg="white", width=15)
b2.place(x=400, y=400)

m3 = Image.open(r"m3.jpg")
mr3 = ImageTk.PhotoImage(m3.resize((201,251)))
photo =Label(a, image=mr3)
photo.place(x=700,y=100)
b3 = Button(a, text="Book", font=("Palatino Linotype", 15), bg="FireBrick", fg="white", width=15)
b3.place(x=700, y=400)

m4 = Image.open(r"m4.jpg")
mr4 = ImageTk.PhotoImage(m4.resize((201,251)))
photo =Label(a, image=mr4)
photo.place(x=1000,y=100)
b4 = Button(a, text="Book", font=("Palatino Linotype", 15), bg="FireBrick", fg="white", width=15)
b4.place(x=1000, y=400)
a.mainloop()
