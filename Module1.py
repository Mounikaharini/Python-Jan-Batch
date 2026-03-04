import random as r
print(r.random())
print(r.randint(1,100))
print(r.randrange(0,100,10))


import sys as s
a=dir(s)
print(a)
print(s.path)
print("---------------------------------------")
print(s.version)
while True:
    print("1.Login\n2.Exit")
    c = int(input("Enter choice (1 / 2)"))
    if c==1:
        print("Logged in")
    elif c==2:
        print("Before exit")
        s.exit(0)
        print("After exit")

import socket
host=socket.gethostname()
print(host)

import pywhatkit
product = input("Enter search data :")
pywhatkit.search(product)

import webbrowser
webbrowser.open_new_tab("https://m.media-amazon.com/images/I/61RFlIUeaIL._SY575_.jpg")

import calendar as c
print(c.month(2023,8))
print(c.isleap(2023))
print(c.calendar(2026))

import time
print(time.ctime())
print("hi")
time.sleep(2)
print("bye")

l = ["Samsung","Lenovo","HP","Mac","Dell","Asus","Acer","VivoBook","Victus","Omen","MI"]
for i in l:
    time.sleep(2)
    print(i)

  
