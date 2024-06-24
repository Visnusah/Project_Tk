from tkinter import *


root = Tk()
root.geometry("500x300")

frame = Frame(root,).grid(row=0,column=0)

def add():
  # root.destroy()
  root1 = Toplevel() # Toplevel()
  lbl = Label(text="Hello").place(x= 10, y= 30)
  btm1 = Button(root1, text="Closed Window", command=root.destroy).place(x=5, y=10)
  



lbl = Label(text='Hello')
btn = Button(frame, text="Click Here", command=add).place(x=150, y=50)

root.mainloop()