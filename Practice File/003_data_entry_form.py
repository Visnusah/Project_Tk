import tkinter as tk #NOTE: tkinter is a module used to create a GUI
from tkinter import * #NOTE: * is used to import all the classes from the module
from tkinter import ttk #IMP: ttk is used to create a combobox

window = tk.Tk()
window.title("Data Entry Form")
# window.geometry("400x350")

# create a main frame for the window //NOTE: Frame is used to create a container
frame = tk.Frame(window)
frame.pack()

FN1 = font=("Arial", 12)
FN2 = font=("Arial", 15, "bold")
# create Label widget

# create frame for user information //NOTE: LabelFrame is used to create a frame with a title(text="")
user_info_frame = tk.LabelFrame(frame, text="User Information", font=FN2)
user_info_frame.grid(row=0, column=0, padx=30, pady=30)



# create Label widget //NOTE: Label widget is used to create a text
first_name = tk.Label(user_info_frame, text="First Name: ", font=FN1)
last_name = tk.Label(user_info_frame, text="Last Name: ", font=FN1)
title = tk.Label(user_info_frame, text="Title", font=FN1)
age = tk.Label(user_info_frame, text="Age: ", font=FN1)
nationality = tk.Label(user_info_frame, text="Nationality: ", font=FN1)

# create Entry widget //NOTE: Entry widget is used to create a text box
first_name_entry = tk.Entry(user_info_frame, font=FN1)
last_name_entry = tk.Entry(user_info_frame, font=FN1)


# create grid for the label //NOTE: grid is used to create a table like structure
first_name.grid(row=0 , column=0)
last_name.grid(row=0 , column=1)
title.grid(row=0, column=2)
age.grid(row=2, column=0)
nationality.grid(row=2, column=1)

# create grid for the entry widget //NOTE: grid is used to create a table like structure
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)



# create a combobox  //IMP: Combobox is used to create a dropdown list
title_combobox = ttk.Combobox(user_info_frame, values=["Mr", "Mrs", "Miss"], font=FN1)
title_combobox.grid(row=1, column=2)

nationality_combobox = ttk.Combobox(user_info_frame, values=["Nepali", "Indian", "American"], font=FN1)
nationality_combobox.grid(row=3, column=1)


# create a spinbox //IMP: Spinbox is used to create a number input field with a range of values from_ and to
age.spinbox = tk.Spinbox(user_info_frame, from_=18, to=50, font=FN1)
age.spinbox.grid(row=3, column=0)


# for better spacing and alignment of the widgets in the frame //IMP: winfo_children() is used to get all the children of the frame
for widget in user_info_frame.winfo_children():
  widget.grid_configure(padx=10, pady=5)


# second frame for contact information

window.mainloop()