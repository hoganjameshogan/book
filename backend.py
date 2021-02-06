import sqlite3 as sq3

class Database:
    def __init__(self, db):
        self.conn = sq3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()
        # conn.close()

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title,author,year,isbn))
        self.conn.commit()
        print("back --> Inserted : {}-{}-{}-{}".format(title,author,year,isbn))

    def view(self):
        c = self.cur.execute("SELECT * FROM books").fetchall()
        self.conn.commit()
        return c

    def update(self,id,title,author,year,isbn):
        print("Updating with {},{},{},{}".format(title,author,year,isbn))
        self.cur.execute("UPDATE books SET \
            title = ? , \
            author = ? , \
            year = ? , \
            isbn = ? \
            WHERE id = ?" , (title,author,year,isbn,id))
        self.conn.commit()

    def search(self,title="",author="",year="",isbn=""):
        cur = self.conn.cursor()
        c = cur.execute("SELECT * FROM books WHERE \
            title=? OR \
            author=? OR \
            year=? OR \
            isbn=? \
            ",(title,author,year,isbn)).fetchall()
        self.conn.commit()
        return c

    def delete(self,id):
        self.cur.execute("DELETE FROM books WHERE id=?", (id,))
        self.conn.commit()

    def del(self):
        self.conn.close()



