import pywhatkit
from tkinter import *
import tkinter.font as font

window = Tk()

window.geometry('500x500')

def text_to_handwriting():

    text = str(e1_value.get())
    filename = str(e2_value.get())

    pywhatkit.text_to_handwriting(text, save_to=filename)

b1 = Button(window, text="Create", command=text_to_handwriting, height=2, width=10, bg='violet', fg='white', font=font.Font(family='century gothic', size=10, weight='bold'), relief=GROOVE)
b1.place(x=10, y=200)

l1 = Label(window, text="Text->")
l1.place(x=10, y=20)

l2 = Label(window, text="File Name->")
l2.place(x=10, y=400)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value, justify='center')
e1.place(x=100, y=10, height=300, width=300)

e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.place(x=100, y=400, height=50, width=200)

window.mainloop()