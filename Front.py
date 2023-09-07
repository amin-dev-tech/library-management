from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Back import *

root = Tk()
root.title("Library Management")
root.resizable(False, False)

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Title", bootstyle="primary").grid(column=0, row=0)
book_name = ttk.Entry(frm, bootstyle=PRIMARY)
book_name.grid(column=1, row=0, pady=5)

ttk.Label(frm, text="Author", bootstyle="primary").grid(column=2, row=0)
author = ttk.Entry(frm, bootstyle=PRIMARY)
author.grid(column=3, row=0, pady=5)

ttk.Label(frm, text="Release Year", bootstyle="primary").grid(column=0, row=1)
year = ttk.Entry(frm, bootstyle=PRIMARY)
year.grid(column=1, row=1, pady=5)

ttk.Label(frm, text="ISBN", bootstyle="danger").grid(column=2, row=1)
isbn = ttk.Entry(frm, bootstyle=DANGER)
isbn.grid(column=3, row=1, pady=5)

scrollbr = Scrollbar(frm, orient="vertical")
scrollbr.grid(column=2, row=2, rowspan=5, sticky=N + S + W)

result = Text(frm, height=10, width=35, yscrollcommand=scrollbr.set)
result.grid(column=0, row=2, columnspan=2, rowspan=5, pady=5)

scrollbr.config(command=result.yview)


def showAll():
    result.insert(END, selectAll())
    print(selectAll())


def insert():
    insert_new(book_name.get(), author.get(), int(year.get()), int(isbn.get()))


def searchBook():
    result.insert(END, search(isbn.get()))


def deleteBook():
    delete(isbn.get())


ttk.Button(frm, text="All Records", command=showAll, cursor="hand2", width=13).grid(
    column=3, row=2
)
ttk.Button(
    frm, text="Search For Books", command=searchBook, cursor="hand2", width=13
).grid(column=3, row=3)
ttk.Button(frm, text="Add New book", command=insert, cursor="hand2", width=13).grid(
    column=3, row=4
)
ttk.Button(
    frm,
    text="Delete A Book",
    command=deleteBook,
    cursor="hand2",
    width=13,
    bootstyle=DANGER,
).grid(column=3, row=5)

ttk.Button(
    frm, text="Quite", command=root.destroy, cursor="hand2", width=13, bootstyle=DARK
).grid(column=3, row=6)


# ttk.Label(frm, text="Library Application").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
