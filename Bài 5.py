from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Hello")
window.geometry('350x200')
lbl = Label(window, text="say hi")
lbl.grid(column=0, row=0)

def clicked():
    chk_state = BooleanVar()# set check state
    chk_state.set(True) # set check state
    chk = Checkbutton(window, text='Choose', var=chk_state)
    chk.grid(column=5, row=5)

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=3, row=4)
window.mainloop()