from tkinter import *


root = Tk()
root.geometry("400x300")


def open_win():
	win = Toplevel()
	win.geometry("200x200")
	win.overrideredirect(1)
	win.after(3000, lambda:win.destroy() )


Button(root, text="Open", command=open_win).place(relx=.5, rely=.5)


root.mainloop()
