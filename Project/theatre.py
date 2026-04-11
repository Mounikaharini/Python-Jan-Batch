import tkinter as tk
from tkinter import *
from tkinter import messagebox

a = tk.Tk()
a.geometry("1400x900")
a.config(bg="#E6E6FA")
a.title("FlickIt: Casual, fun, and tech-friendly")

# Title
l1 = Label(a, text="FlickIt", font=("Palatine Linotype", 40), bg="#E6E6FA", fg="black")
l1.pack()

# Subtitle
l2 = Label(a, text="Choose The Theatre", font=("Palatine Linotype", 30), bg="#E6E6FA", fg="black")
l2.place(x=550, y=100)
def b1form():
    a.destroy()
    import dnc
# Buttons
b1 = Button(a, text="DNC", font=("Palatino Linotype", 20), bg="FireBrick", fg="white", width=25,command=b1form)
b1.place(x=500, y=200)

b2 = Button(a, text="SPR", font=("Palatino Linotype", 20), bg="FireBrick", fg="white", width=25)
b2.place(x=500, y=300)

b3 = Button(a, text="ARRS", font=("Palatino Linotype", 20), bg="FireBrick", fg="white", width=25)
b3.place(x=500, y=400)

b4 = Button(a, text="Divyam", font=("Palatino Linotype", 20), bg="FireBrick", fg="white", width=25)
b4.place(x=500, y=500)

b5 = Button(a, text="Raajam", font=("Palatino Linotype", 20), bg="FireBrick", fg="white", width=25)
b5.place(x=500, y=600)

a.mainloop()
