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

def delete():
    conn = sq3.connect("books.db")
    cur = conn.cursor()
    # cur.execute()
    conn.commit()
    conn.close()


insert("Ulysses", "James Joyce",30000,1.99)
print(view())
connect()

