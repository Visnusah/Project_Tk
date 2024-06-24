
#NOTE:
# create a GUI entry and modify the label text


# from tkinter import *
# root = Tk()
# root.title("GUI")
# root.maxsize(width=600,height=300)
# root.minsize(width=600,height=300)
# #function
# def add():
#   x = var.get()
#   print(x)
#   mylabell.config(text=x,bg="green")

# #label1
# mylabel = Label(root, text="User Name", fg="red",bg="yellow")
# mylabel.grid(row=0, column=0)

# #label2
# mylabel2 = Label(root, text="Password", fg="red",bg="yellow")
# mylabel2.grid(row=2, column=0)

# mylabel = Label(root, text="User Name", fg="red",bg="yellow")
# mylabel.grid(row=0, column=0)


# #label2
# mylabell = Label(root, text="Nothing",fg="red", bg="yellow")
# mylabell.grid(row=0, column=1)

# #entry
# var = StringVar() #IMP: StringVar() is used to get the value from the entry widget
# ent = Entry(root, bg="black", fg='white', textvariable=var) #IMP: textvariable is used to get the value from the entry widget
# ent.grid(row=1, column=0)


# #enrty2
# var2 = StringVar()
# ent2 = Entry(root, bg="black", fg="white", textvariable=var2)
# ent2.grid(row=3, column=0)



# #button
# btn = Button (root, text="Submit", bg="black", command=add)
# btn.grid(row=1, column=1)


# def add():
#   x = var.get()
#   print(x)
  

# root.mainloop()

# NOTE:
# Entry --> input field --> index 0
# text --> multiline text input -> index 1.0(float)
# for indexing in text --> "RAJ" --> 1.0->R, 1.1->A, 1.2->J


from tkinter import *

root = Tk()

def text():
  text1 = "Adderess: " + mytext.get(1.0, END)
  lebelOne.config(text=text1)


mytext = Text(root, width=50, height=10, bg="black", fg="white")
mytext.grid(row=0, column=0)

btmOne = Button(root, text="Submit", command=text)
btmOne.grid(row=1, column=0)


lebelOne = Label(root, text="Nothing")
lebelOne.grid(row=2, column=0)


root.mainloop()



# NOTE:

# from tkinter import *

# root = Tk()
# root.title("GUI")

# l1 = Text(root, width=30, height=5, border=4)
# l1.grid(row=0, column=0)

# e1 = Entry(root, width=30)
# e1.grid(row=0, column=1)

# lbl = Label(root, text="Display here", bg="yellow", fg="red")
# lbl.grid(row=1, column=0)

# def add():
#   text = l1.get(1.0, END).strip() + " " + e1.get()
#   lbl.config(text=text, bg="green", fg="white")
  
# btn = Button(root, text="Submit", command=add)
# btn.grid(row=1, column=1)

# root.mainloop()


