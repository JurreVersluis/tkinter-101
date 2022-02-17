import tkinter
import time
counter = 1
counter2 = 2000
currentWidth = 100
currentHeight = 100
Kleuren = ['white', 'yellow', 'orange', 'red', 'purple', 'black']


def uitbreiden():
    global counter, counter2, currentWidth, currentHeight
    print(6 - (counter))
    window.configure(bg=(Kleuren[counter]))
    window.geometry("{}x{}".format(currentWidth, currentHeight))

    if counter == 5:
        window.after(2000, window.destroy)

    counter += 1
    currentWidth += 50
    currentHeight += 50


window = tkinter.Tk()

window.title('My first window')
window.geometry("50x50")
print('6')
for i in range(5):
    window.after(counter2, uitbreiden)
    counter2 += 2000

window.mainloop()
print('BOEMMMM!!!')


