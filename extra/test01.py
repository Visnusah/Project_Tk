import customtkinter as ck

ck.set_appearance_mode("System")  # Modes: system (default), light, dark
ck.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ck.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = ck.CTkButton(master=app, text="CTkButton", fg_color="red", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=ck.CENTER)

lbl = ck.CTkLabel(master=app, text="CTkLabel", fg_color="black", text_color="White")
lbl.place(relx=0.5, rely=0.3, anchor=ck.CENTER)

app.mainloop()