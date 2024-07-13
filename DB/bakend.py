# QUE: 

from tkinter import *
from tkinter import ttk
import sqlite3 as db

root = Tk()
root.geometry("700x700")
root.resizable(1, 1)
root.title("User Information")

# Database Connection
conn = db.connect("database.db") # IMP: Connect to the databasew
cursor = conn.cursor() # IMP: Cursor object is used to interact with the database

cursor.execute(
  # IMP: Create a table if it does not exist 
    """
    CREATE TABLE IF NOT EXISTS user(
      username TEXT,
      address TEXT,
      role TEXT,
      salary INTEGER
    )
    """
)

conn.commit() # IMP: Commit is used to save the changes
conn.close() # IMP: Close the connection to the database after the operation is done


def add():
  conn = db.connect("database.db")
  cursor = conn.cursor()
  cursor.execute(
    "INSERT INTO  User VALUES(?, ?, ?, ?)",
    (username.get(), address.get(), role.get(), salary.get())
  )
  
  conn.commit()
  conn.close()
  username.delete(0, END) # IMP: Delete the entry after the operation is done
  address.delete(0, END)
  role.delete(0, END)
  salary.delete(0, END)
  retrieve()
  
  
#
def retrieve():
    conn = db.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT *, oid FROM user")
    records = cursor.fetchall()
    
    print(records) # IMP: Print the records in the console
    
    
    # print_records = ""
    # for data in records:
    #     print_records += f"{data[0]} {data[1]} {data[2]} {data[3]} {data[4]}\n"
    # lbl.config(text=print_records)
    # # Clear the Treeview
    # for item in tree.get_children():
    #     tree.delete(item)
    
    for data in records:
        tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4]))
    conn.close()
  
def delete():
    conn = db.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user WHERE oid=" + delete_box.get()) # oid : Object ID
    conn.commit()
    conn.close()
    delete_box.delete(0, END)
    retrieve() # IMP: Call the retrieve function to update the records
    
def update(record_id):
  conn = db.connect("database.db")
  cursor = conn.cursor()
  cursor.execute(
  """
  UPDATE user SET
  username = :username,
  address = :address,
  role = :role,
  salary = :salary
  WHERE oid = :oid
  """,
  {
    'username': username_editor.get(),
    'address': address_editor.get(),
    'role': role_editor.get(),
    'salary': salary_editor.get(),
    'oid': record_id
    
  }
)
  conn.commit()
  conn.close()
  editor.destroy()
  
# NOTE: The global keyword is used in the edit function to allow the function to modify variables that are defined outside of its scope.
def edit():
    global editor
    editor = Tk()
    editor.title("update data")
    editor.geometry("400x400")
    global username_editor
    global address_editor
    global role_editor
    global salary_editor
    conn = db.connect("database.db")
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM user WHERE oid=" + record_id)
    records = c.fetchall()
    username_editor = Entry(editor, width=30)
    username_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=1, column=1)
    role_editor = Entry(editor, width=30)
    role_editor.grid(row=2, column=1)
    salary_editor = Entry(editor, width=30)
    salary_editor.grid(row=3, column=1)
    # Create textbox labels
    username_label = Label(editor, text="USERNAME")
    username_label.grid(row=0, column=0, pady=(10, 0))
    address_label = Label(editor, text="ADDRESS")
    address_label.grid(row=1, column=0)
    role_label = Label(editor, text="ROLE")
    role_label.grid(row=2, column=0)
    salary_label = Label(editor, text="SALARY")
    salary_label.grid(row=3, column=0)
    for record in records:
        username_editor.insert(0, record[0]) # 0 -> is the position where the data is inserted
        address_editor.insert(0, record[1])
        role_editor.insert(0, record[2])
        salary_editor.insert(0, record[3])
    edit_btn = Button(editor, text="SAVE", command= lambda: update(record_id))
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=125)
    
    exit_btn = Button(editor, text="EXIT", command=editor.quit)
    exit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=125)


# Add Treeview widget
tree = ttk.Treeview(root)
tree['columns'] = ('Username', 'Address', 'Role', 'Salary', 'ID')
tree.column("#0", width=0, stretch=NO) # IMP: The first column is hidden and stretch is for the column to be fixed
tree.column("Username", anchor=W, width=120)
tree.column("Address", anchor=W, width=120)
tree.column("Role", anchor=W, width=120)
tree.column("Salary", anchor=W, width=120)
tree.column("ID", anchor=W, width=50)

tree.heading("#0", text="", anchor=W) # IMP: The first column is hidden
tree.heading("Username", text="Username", anchor=W) # IMP: The anchor is used to align the text to the left
tree.heading("Address", text="Address", anchor=W) 
tree.heading("Role", text="Role", anchor=W)
tree.heading("Salary", text="Salary", anchor=W)
tree.heading("ID", text="ID", anchor=W)  

tree.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
  
    
# Labels
label_username = Label(root, text="Username", font=("Arial Bold", 20))
label_username.grid(row=0, column=0, padx=10, pady=10, sticky=W)
label_address = Label(root, text="Address", font=("Arial Bold", 20))
label_address.grid(row=1, column=0, padx=10, pady=10, sticky=W)
label_role = Label(root, text="Role", font=("Arial Bold", 20))
label_role.grid(row=2, column=0, padx=10, pady=10, sticky=W)
label_salary = Label(root, text="Salary", font=("Arial Bold", 20))
label_salary.grid(row=3, column=0, padx=10, pady=10, sticky=W)
label_delete = Label(root, text="Delete ID", font=("Arial Bold", 20))
label_delete.grid(row=4, column=0, padx=10, pady=10, sticky=W)

lbl = Label(root, text="")
lbl.grid(row=8, column=0, padx=10, pady=10, sticky=W)


# Entries
username = Entry(root, width=40)
username.grid(row=0, column=1, padx=10, pady=10)
address = Entry(root, width=40)
address.grid(row=1, column=1, padx=10, pady=10)
role = Entry(root, width=40)
role.grid(row=2, column=1, padx=10, pady=10)
salary = Entry(root, width=40)
salary.grid(row=3, column=1, padx=10, pady=10)
delete_box = Entry(root, width=40)
delete_box.grid(row=4, column=1, padx=10, pady=10)

# Buttons
btn_add = Button(root, text="Add", font=("Arial Bold", 20), command=add)
btn_add.grid(row=5, column=0, padx=10, pady=20, sticky=W)
btn_retrieve = Button(root, text="Retrieve", font=("Arial Bold", 20), command=retrieve)
btn_retrieve.grid(row=5, column=1, padx=10, pady=20, sticky=E)
delete_btn = Button(root, text="Delete", font=("Arial Bold", 20), command=delete).grid(row=6, column=0, padx=10, pady=20, sticky=W)
update_btn = Button(root, text="Update", font=("Arial Bold", 20), command=edit).grid(row=6, column=1, padx=10, pady=20, sticky=E)

# 

EXIT_btn = Button(root, text="Exit", font=("Arial Bold", 20), command=root.quit).grid(row=7, column=0, padx=10, pady=20, sticky=EW)
root.mainloop()