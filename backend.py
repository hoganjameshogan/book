import sqlite3 as sq3

def connect():
    conn = sq3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sq3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title,author,year,isbn))
    conn.commit()
    print("Inserted {}-{}-{}-{}".format(title,author,year,isbn))
    conn.close()

def view():
    conn = sq3.connect("books.db")
    cur = conn.cursor()
    c = cur.execute("SELECT * FROM books").fetchall()
    conn.commit()
    conn.close()
    return c

def update():
    conn = sq3.connect("books.db")
    cur = conn.cursor()
    # cur.execute()
    conn.commit()
    conn.close()

def search(title="",author="",year="",isbn=""):
    conn = sq3.connect("books.db")
    cur = conn.cursor()
    c = cur.execute("SELECT * FROM books WHERE \
        title=? OR \
        author=? OR \
        year=? OR \
        isbn=? \
        ",(title,author,year,isbn)).fetchall()
    conn.commit()
    conn.close()
    return "Returned : {}".format(c)
    

def delete():
    conn = sq3.connect("books.db")
    cur = conn.cursor()
    # cur.execute()
    conn.commit()
    conn.close()


# print(search("Ulysses"))
connect()

