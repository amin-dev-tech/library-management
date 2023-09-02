from tkinter import *
from tkinter import ttk
from Back import *

root = Tk()
root.title(" مدیریت کتابخانه")

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="عنوان").grid(column=0, row=0)
book_name = ttk.Entry(frm)
book_name.grid(column=1, row=0)

ttk.Label(frm, text="نویسنده").grid(column=2, row=0)
author = ttk.Entry(frm)
author.grid(column=3, row=0)

ttk.Label(frm, text="سال انتشار").grid(column=0, row=1)
year = ttk.Entry(frm)
year.grid(column=1, row=1)

ttk.Label(frm, text="ISBN").grid(column=2, row=1)
isbn = ttk.Entry(frm)
isbn.grid(column=3, row=1)

scrollbr = Scrollbar(frm, orient="vertical")
scrollbr.grid(column=2, row=2, rowspan=5, sticky=N + S + W)

result = Text(frm, height=15, width=45, yscrollcommand=scrollbr.set)
result.grid(column=0, row=2, columnspan=2, rowspan=5)

scrollbr.config(command=result.yview)


def showAll():
    result.insert(END, selectAll())


def insert():
    insert_new(book_name.get(), author.get(), int(year.get()), int(isbn.get()))


def searchBook():
    result.insert(END, search(isbn.get()))


def deleteBook():
    delete(isbn.get())


ttk.Button(frm, text="مشاهده همه", command=showAll).grid(column=3, row=2)
ttk.Button(frm, text="جست و جوی کتاب", command=searchBook).grid(column=3, row=3)
ttk.Button(frm, text="اضافه کردن کتاب", command=insert).grid(column=3, row=4)
ttk.Button(frm, text="حذف کردن", command=deleteBook).grid(column=3, row=5)
ttk.Button(frm, text="بستن", command=root.destroy).grid(column=3, row=6)


# ttk.Label(frm, text="Library Application").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
