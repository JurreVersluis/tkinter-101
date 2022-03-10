import tkinter
import tkinter as tk
import random
from tkinter import messagebox as mbox

grabbelton = ['een huis', 'een puppy', 'een Minecraft kopietje', '10.000 in schulde', 'een Bitcoin', 'een hoge hoed',
              'Een ticket voor Katy Perry', 'een schoolgebouw', 'een meet en greet met persoon naar keuze',
              'Mil zijn bidon']



def grabbelen():
    (mbox.showinfo('Je hebt gekregen:', f'Je hebt {grabbelton.pop(random.randrange(0,len(grabbelton)))} gewonnen'))
    hoeveelover.set(len(grabbelton))
    alledingen.set(grabbelton)

window = tk.Tk()

alledingen = tk.StringVar()
alledingen.set(grabbelton)

hoeveelover = tk.StringVar()
hoeveelover.set(len(grabbelton))

window.title('Grabbelton')
window.geometry("900x600")
window.config(bg='grey')

button = tkinter.Button(window)
button.pack(ipadx="150",ipady="15", pady="100")
button.configure(text="Grabbelen",bg='red', command=grabbelen)

label = tk.Label(window, textvariable=alledingen)
label.pack(ipadx="150",ipady="120")
label.configure(bg='blue')

label2 = tk.Label(window, textvariable=hoeveelover)
label2.pack(ipadx="50",ipady="10",pady="20")
label2.configure(bg='green')

window.mainloop()