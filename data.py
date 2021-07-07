import sqlite3 as sql


con = sql.connect("data.db")
cur = con.cursor()

def book_table():
    x = cur.execute("SELECT * FROM book")
    return x


