from tkinter import Tk, Button,Label,Scrollbar,Listbox,StringVar,Entry,W,E,N,S,END
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as pyo

con = pyo.connect("mybooks.db")
#print(con)

cursor = con.cursor()


class Bookdb:
    def __init__(self):
        self.con = pyo.connect("mybooks.db")
        self.cursor = con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, isbn INTEGER)")
        self.con.commit()
        print("You have connected to the database")
        print(con)

    def __del__(self):
        self.con.close()

    def view(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return rows

    def insert(self,title, author, isbn):
        sql=("INSERT INTO books(title,author,isbn)VALUES (?,?,?)")
        values =[title,author,isbn]
        self.cursor.execute(sql,values)
        self.con.commit()
        messagebox.showinfo(title="Book Database",message="New book added to database")

    def update(self, id, title, author, isbn):
        tsql = 'UPDATE books SET  title = ?, author = ?, isbn = ? WHERE id=?'
        self.cursor.execute(tsql, [title,author,isbn,id])
        self.con.commit()
        messagebox.showinfo(title="Book Database",message="Book Updated")

    def delete(self, id):
        delquery ='DELETE FROM books WHERE id = ?'
        self.cursor.execute(delquery, [id])
        self.con.commit()
        messagebox.showinfo(title="Book Database",message="Book Deleted")

db = Bookdb()

def get_selected_row(event):
    global selected_tuple
    index = list_bx.curselection()[0]
    selected_tuple = list_bx.get(index)
    title_entry.delete(0, 'end')
    title_entry.insert('end', selected_tuple[1])
    author_entry.delete(0, 'end')
    author_entry.insert('end', selected_tuple[2])
    isbn_entry.delete(0, 'end')
    isbn_entry.insert('end', selected_tuple[3])

def view_records():
    list_bx.delete(0, 'end')
    for row in db.view():
        list_bx.insert('end', row)

def add_book():
    db.insert(title_text.get(),author_text.get(),isbn_text.get())
    list_bx.delete(0, 'end')
    list_bx.insert('end', (title_text.get(), author_text.get(), isbn_text.get()))
    title_entry.delete(0, "end") # Clears input after inserting
    author_entry.delete(0, "end")
    isbn_entry.delete(0, "end")
    con.commit()

def delete_records():
    db.delete(selected_tuple[0])
    con.commit()

def clear_screen():
    list_bx.delete(0,'end')
    title_entry.delete(0,'end')
    author_entry.delete(0,'end')
    isbn_entry.delete(0,'end')

def update_records():
    db.update(selected_tuple[0], title_text.get(), author_text.get(), isbn_text.get())
    title_entry.delete(0, "end") # Clears input after inserting
    author_entry.delete(0, "end")
    isbn_entry.delete(0, "end")
    con.commit()

def on_closing():
    dd = db
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        app.destroy()
        del dd

app = Tk() 

# Application window GUI - set to specific size that cannot be altered
app.title("My Books Database Application")
app.configure(background="light green")
app.geometry("1000x500")
app.resizable(width=False, height=False)

# Labels and entry widgets

title_label =ttk.Label(app,text="Title",background="light green",font=("TkDefaultFont", 16))
title_label.grid(row=0, column=0, sticky=W)
title_text = StringVar()
title_entry = ttk.Entry(app,width=24,textvariable=title_text)
title_entry.grid(row=0, column=1, sticky=W)

author_label =ttk.Label(app,text="Author",background="light green",font=("TkDefaultFont", 16))
author_label.grid(row=0, column=2, sticky=W)
author_text = StringVar()
author_entry = ttk.Entry(app,width=24,textvariable=author_text)
author_entry.grid(row=0, column=3, sticky=W)

isbn_label =ttk.Label(app,text="ISBN",background="light green",font=("TkDefaultFont", 14))
isbn_label.grid(row=0, column=4, sticky=W)
isbn_text = StringVar()
isbn_entry = ttk.Entry(app,width=24,textvariable=isbn_text)
isbn_entry.grid(row=0, column=5, sticky=W)

# Add a button to insert inputs into database

add_btn = Button(app, text="Add Book",bg="black",fg="black",font="helvetica 10 bold", command=add_book)
add_btn.grid(row=0, column=6, sticky=W)

# Add  a listbox  to display data from database
list_bx = Listbox(app,height=16,width=40,font="helvetica 13",bg="light blue")
list_bx.grid(row=3,column=1, columnspan=14,sticky=W + E,pady=40,padx=15)
list_bx.bind('<<ListboxSelect>>', get_selected_row)

# Add scrollbar to enable scrolling
scroll_bar = Scrollbar(app)
scroll_bar.grid(row=1,column=8, rowspan=14,sticky=W )

list_bx.configure(yscrollcommand=scroll_bar.set) # Enables vetical scrolling
scroll_bar.configure(command=list_bx.yview)

# Add more Button Widgets

modify_btn = Button(app, text="Modify Record",bg="black",fg="black",font="helvetica 10 bold", command=update_records)
modify_btn.grid(row=15, column=4)

delete_btn = Button(app, text="Delete Record",bg="black",fg="black",font="helvetica 10 bold", command=delete_records)
delete_btn.grid(row=15, column=5)

view_btn = Button(app, text="View all records",bg="black",fg="black",font="helvetica 10 bold", command=view_records)
view_btn.grid(row=15, column=1)#, sticky=tk.N)

clear_btn = Button(app, text="Clear Screen",bg="black",fg="black",font="helvetica 10 bold", command=clear_screen)
clear_btn.grid(row=15, column=2)#, sticky=tk.W)

exit_btn = Button(app, text="Exit  Application",bg="black",fg="black",font="helvetica 10 bold", command=app.destroy)
exit_btn.grid(row=15, column=3)


app.mainloop()  # Runs the application until exit

