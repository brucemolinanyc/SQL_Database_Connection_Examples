from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox

app  = Tk()

app.title("My Books Database Application")
app.configure(background="light green")
app.geometry("1000x500")
app.resizable(width=False, height=False)

title_label = ttk.Label(app, text="Title", background="light green", font=("TKDefaultFont", 16))
title_label.grid(row=0, column=0, sticky=W)
title_text = StringVar()
title_entry = ttk.Entry(app, width=24, textvariable=title_text)
title_entry.grid(row=0, column=1, sticky=W)

author_label = ttk.Label(app, text="Author", background="light green", font=("TKDefaultFont", 16))
author_label.grid(row=0, column=2, sticky=W)
author_text = StringVar()
author_entry = ttk.Entry(app, width=24, textvariable=author_text)
author_entry.grid(row=0, column=3, sticky=W)

isbn_label = ttk.Label(app, text="ISBN", background="light green", font=("TKDefaultFont", 14))
isbn_label.grid(row=0, column=4, sticky=W)
isbn_text = StringVar()
isbn_entry = ttk.Entry(app, width=24, textvariable=isbn_text)
isbn_entry.grid(row=0, column=5, sticky=W)

add_btn = Button(app, text="Add Book", background="black", foreground="black", font="helvetica 10 bold", command="")
add_btn.grid(row=0,column=6, sticky=W)

list_box = Listbox(app, height=16, width=40, font="helvetica 13", bg="light blue")
list_box.grid(row=3, column=1, columnspan=14, sticky=W + E, pady=40, padx=15)

scroll_bar = Scrollbar(app)
scroll_bar.grid(row=1, column=8, rowspan=14, sticky=W)

list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_box.yview)

modify_btn = Button(app, text="Modify Record", background="black", foreground="black", font="helvetica 10 bold", command="")
modify_btn.grid(row=15, column=4)

delete_btn = Button(app, text="Delete Record", background="black", foreground="black", font="helvetica 10 bold", command="")
delete_btn.grid(row=15, column=5)

view_btn = Button(app, text="View All Records", background="black", foreground="black", font="helvetica 10 bold", command="")
view_btn.grid(row=15, column=1)

clear_btn = Button(app, text="Clear Screen", background="black", foreground="black", font="helvetica 10 bold", command="")
clear_btn.grid(row=15, column=2)

exit_btn = Button(app, text="Exit Application", background="black", foreground="black", font="helvetica 10 bold", command="")
exit_btn.grid(row=15, column=3)

app.mainloop()