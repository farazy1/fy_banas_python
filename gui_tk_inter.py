from tkinter import *

root = Tk()
a = Label(root, text ="Hello World")
a.pack()
root.title("This is how Python does GUI")
root.geometry("500x250")
root.resizable(width=False, height=False)
root.mainloop()