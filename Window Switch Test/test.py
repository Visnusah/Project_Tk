from tkinter import *



# back to main window
def back():
    root.destroy()
    import batch36uii
    batch36uii.main()


def main():
    global root
    root = Tk()
    root.geometry("500x500")
    root.title("Test Window")
    
    name_label = Label(root, text="This window is from test.py")
    name_label.pack()
    #back to main window btn
    back_btn = Button(root, text="Back", command=back)
    back_btn.pack()
    
    # Exit button to close the window
    exit_btn = Button(root, text="Exit", command=root.destroy)
    exit_btn.pack()
    
    root.mainloop()  # Moved inside the main function
    
if __name__ == "__main__":
    main()