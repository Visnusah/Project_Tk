from customtkinter import (CTk, CTkButton, CTkFrame)

def fun():
    global f1
    f1.destroy()
    f2 = CTkFrame(master=root)
    lbl = CTkButton(root, width=50, height=25,text="Frame Two")
    lbl.pack(expand=True)
    
    f1.mainloop()  
root = CTk()
root.geometry('250x250+100+100')
root.title("Main")

f1 = CTkFrame(master=root)
f1.pack(fill="both", expand=True)
but = CTkButton(master=f1, width=50, height=25,text="TEST frame" ,command=fun).pack(expand=True)

root.mainloop()