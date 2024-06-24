from tkinter import *


root = Tk()
# root.geometry("400x400")
root.title("GUI")
def add():
  print("Hello")
    
add()

# def for new label
def label():
  newLabel1 = Label(root, text="New Label")
  newLabel1.grid(row=1, column=0)


#Entry widget is used to create an input field
newEntry1 = Entry(root, width=50)
newEntry1.grid(row=2, column=0)
  


newBtm1 = Button(root, text="Button one", padx=50, pady=50, fg="red", bg="blue", command=add)
newBtm1.grid(row=0, column=0)

newBtm2 = Button(root, text="Button two", padx=50, pady=50, fg="green", bg="green", command=label)
newBtm2.grid(row=0, column=1)



def newClick():
  newLabelOne = Entry(root, text="Get" + newEntry1.get()).grid(row=3, column=0)

newEntry2 = Entry(root, text="Click", Command=newClick)
newEntry2.grid(row=4, column=0)



root.mainloop()
