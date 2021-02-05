from tkinter import *

import backend as back

win = Tk()
win.title("Book")

#define labels

titleLabel = Label(text="Title")
titleLabel.grid(row=0,column=0)

yearLabel = Label(text="Year")
yearLabel.grid(row=1,column=0)

authorLabel = Label(text="Author")
authorLabel.grid(row=0,column=2)

isbnLabel = Label(text="ISBN")
isbnLabel.grid(row=1,column=2)

#define text entries

titleText = StringVar()
titleEntry = Entry(win,textvariable=titleText)
titleEntry.grid(row=0,column=1)

yearText = StringVar()
yearEntry = Entry(win,textvariable=yearText)
yearEntry.grid(row=1,column=1)

authorText = StringVar()
authorEntry = Entry(win,textvariable=authorText)
authorEntry.grid(row=0,column=3)

isbnText = StringVar()
isbnEntry = Entry(win,textvariable=isbnText)
isbnEntry.grid(row=1,column=3)

#define list box and scroll bar

list1 = Listbox(win,height=6,width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

scroll1 = Scrollbar(win)
scroll1.grid(row=2, column=2)

list1.configure(yscrollcommand=scroll1.set)
scroll1.configure(command=list1.yview)

#define buttons

b1 = Button(win, text="View All", width=12)
b1.grid(row=2,column=3)

b2 = Button(win, text="Search", width=12)
b2.grid(row=3,column=3)

b3 = Button(win, text="Add", width=12)
b3.grid(row=4,column=3)

b4 = Button(win, text="Updated", width=12)
b4.grid(row=5,column=3)

b5 = Button(win, text="Delete", width=12)
b5.grid(row=6,column=3)

b6 = Button(win, text="Close", width=12)
b6.grid(row=7,column=3)

win.mainloop()