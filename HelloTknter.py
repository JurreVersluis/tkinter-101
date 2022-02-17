import tkinter as tk

window = tk.Tk()
window.title('Hello')
window.geometry("300x200")
window.config(bg="Yellow")

box1 = tk.Label(
    window,
    text="Hello Tkinther!",
    bg="green",
    fg="red")

box1.config(font=("Courier", 20))

box1.pack(
    ipadx=10,
    ipady=70,
    expand=True
)

window.mainloop()