 
from tkinter import *



 
def open_batch36uii():
    roots.destroy()
    import test
    test.main()
    
 
def main():
    global roots
    roots = Tk()
    roots.geometry("500x500")
    lbl = Label(roots, text="This is main Window")
    lbl.pack(anchor=W)
 
    btn = Button(roots, text="Login", command=open_batch36uii)
    btn.pack()
    roots.mainloop()
 
 
if __name__ == "__main__":
    main()