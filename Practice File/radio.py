# from tkinter import *

# root = Tk()
# root.geometry("400x300")

# def add():
#   value = var.get()
#   # print(value)
#   # print(var.get())
#   label.config(text=f"{value}")

# label = Label(root, text="values")
# label.pack(anchor=W)


# var = IntVar()
# r1 = Radiobutton(root, text="Male", variable=var, value=1, command=add)
# r1.pack(anchor=W)

# r2 = Radiobutton(root, text="Male", variable=var, value=2, command=add)
# r2.pack(anchor=W)

# root.mainloop()


# NOTE: This is the same code as above but the only difference is the value of the radio button.
from tkinter import *

root = Tk()
root.geometry("400x300")

def add():
  value = var.get()
  # print(value)
  # print(var.get())
  label.config(text=f"{value}")

label = Label(root, text="values")
label.pack(anchor=W)


var = StringVar()
r1 = Radiobutton(root, text="Music", variable=var, value="Music", command=add)
r1.pack(anchor=W)

r2 = Radiobutton(root, text="Football", variable=var, value="Football", command=add)
r2.pack(anchor=W)

btn = Button(root, text="Submit", command=add)
btn.pack(anchor=W)

root.mainloop()


# NOTE: This is the same code as above but the only difference is the value of the radio button.
# from tkinter import *

# root = Tk()
# root.geometry("400x300")

# def add():
#     value = var.get()
#     label.config(text=f"Selected: {value}")

# label = Label(root, text="values")
# label.pack(anchor=W)

# var = StringVar()
# r1 = Radiobutton(root, text="Music", variable=var, value="Music")
# r1.pack(anchor=W)

# r2 = Radiobutton(root, text="Football", variable=var, value="Football")
# r2.pack(anchor=W)

# btn = Button(root, text="Submit", command=add)
# btn.pack(anchor=W)

# root.mainloop()


# IMP: 
# from tkinter import *
# root = Tk()
# root.geometry("400x300")


# def add():
#   if a.get() == 1 and b.get() == 1:
#     lbl.config(text="Music and football")
#   elif a.get() == 1 and b.get() == 0:
#     lbl.config(text="Music")
#   elif a.get() == 0 and b.get() == 1:
#     lbl.config(text="football")


# lbl = Label(text="")
# lbl.pack()

# a = IntVar()
# checkbox_one = Checkbutton(root, text="Music", variable=a)
# checkbox_one.pack()

# b = IntVar()
# checkboxTwo = Checkbutton(root, text="Music", variable=b)
# checkboxTwo.pack()

# btn = Button(root, text="submit", command=add).pack()

# root.mainloop()


# root.mainloop()




# IMP: Show password and hide 
# from tkinter import *

# def toggle_password():
#     if show_password.get():
#         Password.config(show="")
#     else:
#         Password.config(show="*")

# root = Tk()
# root.geometry("400x300")

# Password = Entry(root, show="*")
# Password.pack()

# show_password = IntVar()
# check = Checkbutton(root, text="Show Password", variable=show_password, command=toggle_password)
# check.pack()

# root.mainloop()


# IMP:
# from tkinter import *
# from PIL import Image, ImageTk

# root = Tk()
# root.title("Macbook Air Mac")

# root.geometry("500x300")
# root.resizable(0,0)


# imageThree = ImageTk.PhotoImage(Image.open("Practice File/icon.png")) # open the image
# User_icon = Label(root, image = imageThree) # attach the image to a label
# User_icon.image = imageThree # keep a reference to the image object to prevent garbage collection by python
# User_icon.pack() # place the label in the window


# l1 = Label(root, text="MACBOOK M2").place(x = 200, y= 140)
# # my_image = Image.open("Practice File/icon.png")

# root.mainloop()


