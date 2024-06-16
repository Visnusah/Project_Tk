import tkinter



frame = tkinter.Tk()
frame.title("Login Page")
frame.geometry("340x440")
frame.configure(bg="#f0f0f0")

frame = tkinter.Frame(frame, bg="#f0f0f0", pady=20, padx=20)

font1 = ("Arial", 20) # creating a font object,
font2 = ("Arial", 12) # creating a font object,

bl = "#000000"  # black color


# creating a label widget
login_label = tkinter.Label(frame, text="Login", bg="#f0f0f0", font = font1)
username_label = tkinter.Label(frame, text="Username", bg="#f0f0f0", fg = bl, font = font1 )
username_entry = tkinter.Entry(frame, bg="#f0f0f0", fg=bl, font = font2)
password_entry = tkinter.Entry(frame, show="*",font=font2, bg = "#f0f0f0")
password_label = tkinter.Label(frame, text="Password", bg="#f0f0f0", fg=bl, font = font1 )
login_button = tkinter.Button(frame, text="Login", bg="#ff3399", fg="white", font = font2)

# placing the widgets on the frame
login_label.grid(row=0, column=0, columnspan=2, sticky="ew")
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, columnspan=2)

frame.pack( fill="both", expand=True)

frame.mainloop()