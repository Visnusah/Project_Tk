# Hello Team, I have created a login page using the customtkinter library.
# The customtkinter library is a custom version of the tkinter library which has some additional features.
import tkinter as TK
from customtkinter import *
from PIL import Image, ImageTk # Import the Image and ImageTk modules from the PIL library, (Pillow library)
import ttkbootstrap as ttk
from ttkbootstrap import *


# Initialize the main application window
app = CTk() 
app.geometry("500x400")
app.title("Login Page")
set_appearance_mode("light")  # Set the appearance mode to dark

# Load and set the background image
bg_image = Image.open("background.png")
bg_image = bg_image.resize((800, 600))
bg_image = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
bg_label = TK.Label(app, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame for the login widgets
login_frame = CTkFrame(master=app, width=450, height=350, corner_radius=15)
login_frame.place(relx=0.5, rely=0.5, anchor=TK.CENTER)

# Add a logo or an image above the login form
logo_img = Image.open("logo.png") # Load the image
logo_img = logo_img.resize((300, 300)) # Resize the image
logo_img = CTkImage(dark_image=logo_img, light_image=logo_img) # Create a custom image object

# Create a label to display the logo
logo_label = CTkLabel(master=login_frame, image=logo_img,text=" ")
logo_label.place(relx=0.5, rely=0.15, anchor=TK.CENTER) # Place the logo in the frame

# Add a welcome message
login_msg = CTkLabel(master=login_frame, text="Welcome to login page!", font=("Arial", 25, "bold"))
login_msg.place(relx=0.5, rely=0.25, anchor=TK.CENTER) # Place the message in the frame

# Create entry fields for username and password
username = CTkEntry(master=login_frame, corner_radius=20, border_color="black", border_width=1.2, placeholder_text="Enter your username", width=300, height=40 )
password = CTkEntry(master=login_frame, corner_radius=20, border_color="black", border_width=1.2, placeholder_text="Enter your password", show="*", width=300, height=40)

# Place the entry fields in the frame
username.place(relx=0.5, rely=0.43, anchor=TK.CENTER)
password.place(relx=0.5, rely=0.65, anchor=TK.CENTER)

# Create Login and Register buttons
btn = CTkButton(master=login_frame, text="Login", corner_radius=20, fg_color="white", hover_color="#DBDBDB", border_color="black", border_width=1.2, text_color="black", width=140, height=30)
btn_reg = CTkButton(master=login_frame, text="Register", corner_radius=20, fg_color="white", hover_color="#DBDBDB", border_color="black", border_width=1.2, text_color="black", width=140, height=30)

# Place the buttons in the frame
btn.place(relx=0.3, rely=0.85, anchor=TK.CENTER)
btn_reg.place(relx=0.7, rely=0.85, anchor=TK.CENTER)

btm = ttk.Button(master=login_frame, text="Submit", bootstyle="success")
btm.place(relx=0.3, rely=0.95, anchor=TK.CENTER)
btm_reg = ttk.Button(master=login_frame, text="Cancel", bootstyle="secondary")
btm_reg.place(relx=0.7, rely=0.95, anchor=TK.CENTER)

tog = ttk.Checkbutton(master=login_frame ,bootstyle="round-toggle", text="Remember Info?")
tog.place(relx=0.5, rely=0.75, anchor=TK.CENTER)

# app.state("zoomed")  # Maximize the window
app.mainloop()  # Start the main loop