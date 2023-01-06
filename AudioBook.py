from tkinter import *
import tkinter as tk
root = tk.Tk()
from tkinter.filedialog import askopenfilenames
import pyttsx3
import PyPDF2

root.geometry('400x200')
root.title("AudioBook")

def select_file():
    global file_names
    file_names = askopenfilenames(initialdir = "/", title="select files")

def read_pdf():
    book = open('C:\\Users\\HP\\Desktop\\research paper.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print(pages)
    speaker = pyttsx3.init()
    page = pdfReader.getPage(3)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

Label(root,text="Audiobook",font = "italic 15 bold").pack(pady=10)

Button(root,text = "select pdf file",relief = "solid",command=select_file,font=14).pack(pady=10)
Button(root,text = "start",relief = "solid",command =read_pdf,bg="white",font=15).pack(pady=10)


root.mainloop()