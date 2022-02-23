import tkinter
import tkinter as tk
from datetime import datetime


def klok():
    global Textvar
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    Textvar = tkinter.StringVar(value=current_time)
    box1.config(textvariable=Textvar)
    window.after(1, klok)


window = tk.Tk()

window.title('Klok')
window.geometry("500x200")

Textvar = tkinter.StringVar(value="test")

box1 = tk.Label(
    window,
    bg="#4D5061",
    fg="#A7CAB1")

box1.config(textvariable=Textvar, font=("Courier",40))

box1.pack(
    ipadx=2000,
    ipady=2000,
    expand=True
)

window.after(1,klok)

window.mainloop()

