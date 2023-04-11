from tkinter import *
from tkinter import ttk

root = Tk()
root.title('あぷり～')

# Frame as Widget Container
frame1 = ttk.Frame(root)
frame1.grid()

# Label 1

label1 = ttk.Label(
    frame1,
    width = 50,
    text='どちらか選んでください！！')
label1.grid(row=1,column=1)

def button1_clicked():
    root.quit()
    
icon1 = PhotoImage(file='IMG_0018.gif')

def button1_clicked():
    root.quit()

button1 = ttk.Button (
    frame1,
    image = icon1,
    text = 'VPN',
    compound = TOP,
    command = button1_clicked)
button1.grid(row=2,column=1)

button2 = ttk.Button (
    frame1,
    image = icon1,
    text = 'SSO',
    compound = TOP,
    command = button1_clicked)
button2.grid(row=2,column=2)

root.mainloop()
