import tkinter as tk 
import requests 
import time

canvas = tk.Tk()
canvas.geometry("600*500)")
canvas.title("WEATHER APP")

f=("poppins",15,"bold")
t=("poppins",35,"bold")

textfield=tk.Entry(canvas,font = t)
textfield.pack(paddy = 20)

label1 = tk.label(canvas,font=t)
label1.pack()

label2 = tk.label(canvas,font=f)
label2.pack()

canvas.mainloop()

