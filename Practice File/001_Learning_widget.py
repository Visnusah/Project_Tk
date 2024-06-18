import tkinter as tk

app = tk.Tk()
app.title("Button Widget")
app.geometry("400x350")


font1 = ("Arial", 12)



# create a button
# red_butoon = tk.Button(app, text="Red Bt", bg="white", fg="red", height=2, width=10, font=font1 )
# green_butoon = tk.Button(app, text="Green Bt", bg="green", fg="green", height=2, width=10, font=font1)
# black_butoon = tk.Button(app, text="Black Bt", bg="black", fg="black", height=2, width=10, font=font1 )
# orange_butoon = tk.Button(app, text="Black Bt", bg="black", fg="#D29922", height=2, width=10, font=font1)

# pack the button for display on the window
# red_butoon.pack(side="left")
# green_butoon.pack(side="right")
# black_butoon.pack(side="top")
# orange_butoon.pack(side="bottom")

# create Entry widget from pack method
# user_Name = tk.Label(app, text="User Name", font=font1).pack()
# user_Name = tk.Entry(app, width=30, font=font1).pack()
# password_text = tk.Label(app, text="Password", font=font1).pack()
# Password = tk.Entry(app, width=30, font=font1).pack()
 
# create Entry widget from place
userName = tk.Label(app, text="User Name", font=font1)
address = tk.Label(app, text="Address", font=font1)
contact = tk.Label(app, text="Contact", font=font1)
User_Entry = tk.Entry(app, width=30, font=font1)
address_Entry = tk.Entry(app, width=30, font=font1)
contact_Entry = tk.Entry(app, width=30, font=font1)




# place the label for display on the window
userName.place(x=30, y=50)
address.place(x=30, y=90)
contact.place(x=30, y=130)
User_Entry.place(x=100, y=50)
address_Entry.place(x=100, y=90)
contact_Entry.place(x=100, y=130)


app.mainloop()