import tkinter as tk
from tkinter import *
from tkinter import messagebox

a = tk.Tk()
a.geometry("1400x900")
a.config(bg="#E6E6FA")
a.title("FlickIt: Casual, fun, and tech-friendly")

# Title
title = Label(a, text="LOGIN", font=("Palatino Linotype", 40), bg="#E6E6FA", fg="black")
title.pack()

# Username
usernameLabel = Label(a, text="Name", font=("Palatino Linotype", 15), bg="#E6E6FA", fg="black")
usernameLabel.place(x=550, y=200)

usernameEntry = Entry(a, font=("Palatino Linotype", 20), bg="white", fg="black")
usernameEntry.place(x=550, y=250)

# Email
emailLabel = Label(a, text="Mail", font=("Palatino Linotype", 15), bg="#E6E6FA", fg="black")
emailLabel.place(x=550, y=300)

emailEntry = Entry(a, font=("Palatino Linotype", 20), bg="white", fg="black")
emailEntry.place(x=550, y=350)

# Phone
phoneLabel = Label(a, text="Mobile", font=("Palatino Linotype", 15), bg="#E6E6FA", fg="black")
phoneLabel.place(x=550, y=400)

phoneEntry = Entry(a, font=("Palatino Linotype", 20), bg="white", fg="black")
phoneEntry.place(x=550, y=450)

# Submit function
def submit():
    username = usernameEntry.get()
    email = emailEntry.get()
    phone = phoneEntry.get()

    if username == "" or email == "" or phone == "":
        messagebox.showwarning("LOGIN", "Login Terminated: Fill all the details")
    else:
        if email.endswith("@gmail.com") and phone.isdigit() and len(phone) == 10:
            messagebox.showinfo("LOGIN", "Login Successful")
            a.destroy()
            import theatre
        else:
            messagebox.showerror("LOGIN", "Login Terminated: Enter valid data")

# Submit Button
submitButton = Button(a, text="Submit", command=submit,
                      font=("Palatino Linotype", 20),
                      bg="Firebrick", fg="white")

submitButton.place(x=570, y=520)

a.mainloop()