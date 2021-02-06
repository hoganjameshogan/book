#!/usr/bin/python
# -*- coding: ascii -*-
import os, sys
from tkinter import *
from tkinter import messagebox


from backend import Database

db = Database("books.db")

win = Tk()
# win['bg'] = "#038cfc"
win.title("Book")

def get_selected_row(event):
    global selected
    try:
        idx = list1.curselection()[0]
        selected = list1.get(idx) 
        titleEntry.delete(0,END)
        titleEntry.insert(END,selected[1])
        yearEntry.delete(0,END)
        yearEntry.insert(END,selected[2])
        authorEntry.delete(0,END)
        authorEntry.insert(END,selected[3])
        isbnEntry.delete(0,END)
        isbnEntry.insert(END,selected[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in db.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in db.search(titleText.get(),authorText.get(),yearText.get(),isbnText.get()):
        # print(back.search(title,author,year,isbn))
        list1.insert(END, row)

def insert_command():
    list1.delete(0, END)
    title = titleText.get()
    db.insert(title,authorText.get(),yearText.get(),isbnText.get())
    print("Inserted [{},{},{},{}]".format(titleText.get(),authorText.get(),yearText.get(),isbnText.get()))
    if title == "":
        title = "Untitled Book"
    messagebox.showinfo(title="Success", message="Added {}".format(title))
    titleEntry.delete(0, END)
    authorEntry.delete(0,END)
    yearEntry.delete(0, END)
    isbnEntry.delete(0,END)

def update_command():
    db.update(selected[0],titleText.get(),authorText.get(),yearText.get(),isbnText.get())

def delete_command():
    id = selected[0]
    db.delete(id)
    # list1.delete(selected, )

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

list1.bind('<<ListboxSelect>>', get_selected_row)

#define buttons

b1 = Button(win, text="View All", width=12, command=view_command)
b1.grid(row=2,column=3)

b2 = Button(win, text="Search", width=12, command=search_command)
b2.grid(row=3,column=3)

b3 = Button(win, text="Add", width=12, command=insert_command)
b3.grid(row=4,column=3)

b4 = Button(win, text="Update", width=12, command=update_command)
b4.grid(row=5,column=3)

b5 = Button(win, text="Delete", width=12, command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(win, text="Close", width=12, command=win.destroy)
b6.grid(row=7,column=3)

win.mainloop()


