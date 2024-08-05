from customtkinter import (CTk, CTkButton)

def fun():
    root.destroy()
    inp = CTk()
    inp.mainloop()

root = CTk()
root.geometry('250x250+100+100')
but = CTkButton(master=root, width=50, height=25,text="TEST" ,command=fun).pack(expand=True) 
   
root.mainloop()