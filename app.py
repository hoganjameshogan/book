from tkinter import *

win = Tk()
win.wm_title = "Book"

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

win.mainloop()