import sqlite3 as sq3

class Database:
    def __init__(self, db):
        conn = sq3.connect(db)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        conn.commit()
        conn.close()

    def insert(self,title,author,year,isbn):
        conn = sq3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title,author,year,isbn))
        conn.commit()
        print("back --> Inserted : {}-{}-{}-{}".format(title,author,year,isbn))
        conn.close()

    def view(self):
        conn = sq3.connect("books.db")
        cur = conn.cursor()
        c = cur.execute("SELECT * FROM books").fetchall()
        conn.commit()
        conn.close()
        return c

    def update(self,id,title,author,year,isbn):
        print("Updating with {},{},{},{}".format(title,author,year,isbn))
        conn = sq3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE books SET \
            title = ? , \
            author = ? , \
            year = ? , \
            isbn = ? \
            WHERE id = ?" , (title,author,year,isbn,id))
        conn.commit()
        conn.close()

    def search(self,title="",author="",year="",isbn=""):
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
        return c

    def delete(self,id):
        conn = sq3.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM books WHERE id=?", (id,))
        conn.commit()
        conn.close()



