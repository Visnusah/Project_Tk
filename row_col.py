import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.title("Row and Column")
# root.geometry("580x400")

fontBold = ("Arial", 15, "bold")
fontNormal = ("Arial", 13)

frame = tk.Frame(root)
frame.pack()

info_frame = tk.LabelFrame(frame, text="User Information", font=fontBold)
info_frame.grid(row=0, column=0, padx=30, pady=30)    

l1 = tk.Label(info_frame, text="First Name: ",font=fontNormal).grid(row=0, column=0)
l2 = tk.Label(info_frame, text="Last Name: ",font=fontNormal).grid(row=0, column=1)
l3 = tk.Label(info_frame, text="Age",font=fontNormal).grid(row=0, column=2)

e1 = tk.Entry(info_frame).grid(row=1, column=0)
e2 = tk.Entry(info_frame).grid(row=1, column=1)
e3 = tk.Spinbox(info_frame,font=fontNormal, from_=18, to=50).grid(row=1, column=2)

l4 = tk.Label(info_frame, text="Nationality: ").grid(row=2, column=0)
e4 = ttk.Combobox(info_frame, values=["Nepali", "Indian", "Chinese"],font=fontNormal).grid(row=3, column=0)

for widget in info_frame.winfo_children():
  widget.grid_configure(padx=5, pady=5)
  
  
contact_frame = tk.LabelFrame(frame, text="Contact Information", font=fontBold)
contact_frame.grid(row=0, column=1)

number_label = tk.Label(contact_frame, text="Phone Number: ", font=fontNormal).grid(row=0, column=0)
email_label = tk.Label(contact_frame, text="Email: ", font=fontNormal).grid(row=1, column=0)
telephone_label = tk.Label(contact_frame, text="telephone: ", font=fontNormal).grid(row=2, column=0)



number_label_entry = tk.Entry(contact_frame).grid(row=0, column=1)
email_label_entry = tk.Entry(contact_frame).grid(row=1, column=1)
telephone_label_entry = tk.Entry(contact_frame).grid(row=2, column=1)

for widget in contact_frame.winfo_children():
  widget.grid_configure(padx=5, pady=5)
  
root.state("zoomed")

root.mainloop()