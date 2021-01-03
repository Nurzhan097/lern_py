from tkinter import *
import time

# create main window
from tkinter import ttk

root = Tk()

root.title("first GUI app")             # name
root.iconbitmap("calculator.ico")       # icon
root.geometry("800x600+500+300")        # window size
# root.resizable(0, 0)                    # resize
# root.config(bg="#777")                  # background


f_menu = Frame(root, bg="grey", height=40)
f_menu.pack(fill=X)

l_menu = Label(f_menu, text="Menu", bg="#2b3239", fg="#c6dec1", font="Arial 10")
l_menu.place(x=10, y=10)


# text frame
f_text = Frame(root,)
f_text.pack(fill=BOTH, expand=1)



# run
root.mainloop()
