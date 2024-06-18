# Hello my friends
# this is a short tutorial for how to print hello world in python using tkinter module 

# first we need to import the tkinter module


import tkinter as tk

# then we need to create a window
root = tk.Tk()
# root.iconbitmap("icon.ico")








# set the geometry and title of the window
root.title("Hello World")
# root.geometry("400x350")

# root.resizable(False, False)
# root.resizable(0,0)

# root.maxsize(400,350) # set the maximum size of the window , width = 400, height = 350
# root.minsize(200, 250) # set the minimum size of the window , width = 400, height = 350
# root.state("zoomed") # maximize the window




# create a label
label = tk.Label(root, text="Hello World") # create a label with text "Hello World"

# pack the label for display on the window
label.pack()

# run the main loop for the window to display

root.mainloop()
