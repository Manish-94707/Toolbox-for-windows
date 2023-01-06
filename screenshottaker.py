import pyautogui
import tkinter as Tk
from tkinter.filedialog import *

root=Tk.Tk()

canvas1= Tk.Canvas(root,width = 100, height = 100,bg="black")
canvas1.pack()

def takescreenshot():
    myscreenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myscreenshot.save(save_path+"_screenshot.png")

myButton = Tk.Button(text = "take screenshot", command = takescreenshot,font=10,bg= "Red")
canvas1.create_window(60,60,window=myButton)

root.mainloop()