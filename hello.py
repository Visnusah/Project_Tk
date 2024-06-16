# Hello my friends
# this is a short tutorial for how to print hello world in python using tkinter module 

# first we need to import the tkinter module


import tkinter as tk

# then we need to create a window
root = tk.Tk()


# set the geometry and title of the window
root.geometry("400x350")
root.title("Hello World")


# create a label
label = tk.Label(root, text="Hello World") # create a label with text "Hello World"

# pack the label for display on the window
label.pack()

# run the main loop for the window to display

root.mainloop()
