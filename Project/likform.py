
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import *
from tkinter.ttk import Combobox

a = tk.Tk()
a.geometry("1400x900")
a.config(bg="#E6E6FA")
a.title("FlickIt: Casual, fun, and tech-friendly")

bg = Image.open(r"bg.jpg")
bg = ImageTk.PhotoImage(bg.resize((1600,900)))
photo = Label(a, image=bg)
photo.pack()
#place(relwidth=1,relheight=1)


movie = Label(a, text="LIK : Love Insurance Kompany", font=("Palatine Linotype", 20), bg="FireBrick", fg="#E6E6FA")
movie.place(x=50, y=50)

title = Label(a, text="102K+ are interested , Rating will appear once more reviews come in.", font=("Palatine Linotype", 15), bg="black", fg="#E6E6FA")
title.place(x=50, y=100)

lik1 = Image.open(r"lik1.jpg")
lik1 = ImageTk.PhotoImage(lik1.resize((200,260)))
photo =Label(a, image=lik1)
photo.place(x=50,y=150)

lik2 = Image.open(r"lik2.jpg")
lik2 = ImageTk.PhotoImage(lik2.resize((200,260)))
photo =Label(a, image=lik2)
photo.place(x=280,y=150)

lik3 = Image.open(r"m1.jpg")
lik3 = ImageTk.PhotoImage(lik3.resize((200,260)))
photo =Label(a, image=lik3)
photo.place(x=510,y=150)

details="2h 36m 2D Tamil,Telugu\n•UA13+ •10 Apr, 2026 \n•Comedy,Romantic,Sci-Fi "

detailsLabel = Label(a, text=details, font=("Palatino Linotype", 15), bg="black", fg="white")
detailsLabel.place(x=250, y=450)
about = """About the movie
In a world where everything can be insured, a company dares
to insure love. An app predicts heartbreak and controls
relationships through calculated risk. The voice behind
it believes love is just data until he feels it himself.

When the system flags his own relationship as a failure,
it begins pulling them apart. He discovers the app doesn't
just predict love, it manipulates it. Now, he must choose
between the system the whole world believes in,set in 2040
and the heart and the purest form of love he can't silence.
"""
aboutLabel = Label(a, text=about, font=("Palatino Linotype", 15), bg="black", fg="white")
aboutLabel.place(x=100, y=550)
# Name
usernameLabel = Label(a, text="Name", font=("Palatino Linotype", 15), bg="black", fg="white")
usernameLabel.place(x=970, y=30)

usernameEntry = Entry(a, width=30 ,font=("Palatino Linotype", 15), bg="white", fg="black")
usernameEntry.place(x=850, y=80)


# Phone
phoneLabel = Label(a, text="Mobile", font=("Palatino Linotype", 15), bg="black", fg="white")
phoneLabel.place(x=970, y=130)

phoneEntry = Entry(a, width=30 ,font=("Palatino Linotype", 15), bg="white", fg="black")
phoneEntry.place(x=850, y=180)

# Screen
screenLabel = Label(a, text="Select Available Screen", font=("Palatino Linotype", 15), bg="black", fg="white")
screenLabel.place(x=890, y=230)

screenEntry=Combobox(a,width=31,font=("Palatino Linotype", 13))
screenEntry["values"]=("select screen","skyline screen","ripple screen","space screen","orient screen","pixel screen")
screenEntry.current(0)
screenEntry.place(x=850,y=280)


# Timing
timingLabel = Label(a, text="Timing", font=("Palatino Linotype", 15), bg="black", fg="white")
timingLabel.place(x=970, y=330)

timingEntry=Combobox(a,width=31,font=("Palatino Linotype", 13))
timingEntry["values"]=("select","11.00 A.M","2.30 P.M","6.00 P.M","10.00 P.M")
timingEntry.current(0)
timingEntry.place(x=850,y=380)

# Ac type
acLabel = Label(a, text="Select AC type", font=("Palatino Linotype", 15), bg="black", fg="white")
acLabel.place(x=940, y=430)

option = tk.StringVar()

acEntry = Radiobutton(a, width=13, variable = option,text="A.C", value=1, font=("Palatino Linotype", 11), fg="black", bg="white")
acEntry.place(x=850, y=480)
non_acEntry = Radiobutton(a, width=13,text="Non - A.C", variable = option, value=0, font=("Palatino Linotype", 11), fg="black", bg="white")
non_acEntry.place(x=1000, y=480)

# Seats
seatsLabel = Label(a,text="No.Of.Seats", font=("Palatino Linotype", 15), bg="black", fg="white")
seatsLabel.place(x=940, y=530)

seatsEntry = Spinbox(a, width=32 ,from_=0, to=10, font=("Palatino Linotype", 13), bg="white", fg="black")
seatsEntry.place(x=850, y=580)

def submit():
    name = usernameEntry.get()
    phone = int(phoneEntry.get())
    screen = screenEntry.get()
    time = timingEntry.get()
    seats = int(seatsEntry.get())
    price = seats * 100
    ac = option.get()
    ac_data=""
    if ac=='1':
        ac_data="A.C"
    elif ac=='0':
        ac_data="Non - A.C"
    data = (name,phone,screen,time,seats,price,ac_data)
    messagebox.showinfo("Price", data)
    
    import pymysql as p
    db = p.connect(
        host="localhost",
        user="root",
        password="root",
        database="flickit")
    
    cursor = db.cursor()
    
    query1="""INSERT INTO booking(NAME, Mobile, Screen, Time,Seats , Price, AC )
    VALUES('%s','%d','%s','%s','%d','%d','%s')"""%(name,phone,screen,time,seats,price,ac_data)
    try:
        cursor.execute(query1)
        db.commit()
        messagebox.showinfo("Booking","Ticket Booked")
    except Exception as e:
        db.rollback()
        messagebox.showerror("Booking",e)
        db.close()


#Book button
bookButton = Button(a, text="Book", font=("Palatino Linotype", 15), bg="FireBrick", fg="white", width=25 , command=submit)
bookButton.place(x=850, y=630)

a.mainloop()
















