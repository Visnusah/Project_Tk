import tkinter as tk
from tkinter import *
# from PIL import ImageTk


app = tk.Tk()



# img = tk.Image("photo", file="icon.png")
# root.iconphoto(True, img) # you may also want to try this.
# app.tk.call('wm','iconphoto', app._w, img)

# app.master.iconbitmap("my_icon.ico")
app.wm_iconbitmap('Icon.ico')

app.title("Form Application")
app.geometry("400x350")

font1 = ("Arial", 12)
# app.iconbitmap('icon.png')
# app.iconphoto(False, tk.PhotoImage(file="icon.png"))



# Creating a form

# create Label widget
student_Name = tk.Label(app, text="Student Name: ", font=font1)
student_address = tk.Label(app, text="Address: ", font=font1)
#  = tk.Label(app, text="", font=font1)

# create Entry widget
student_Entry = tk.Entry(app, width=30, font=font1, )


# place the label for display on the window
student_Name.place(x=30, y=50)
student_Entry.place(x=115, y=50)

student_Entry.insert(0, "student Name")


def clear(event):
    if student_Entry.get() == "student Name":
        student_Entry.delete(0, tk.END)

student_Entry.bind('<FocusIn>', clear)

app.mainloop()