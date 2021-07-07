import sqlite3 as sql


con = sql.connect("data.db")
cur = con.cursor()

lst = ["2",'How to Think Like a Computer Scientist', "Rick Ashley", "https://blink", "Computer Science", "https://plink"]
#cur.execute(f"INSERT INTO book VALUES {tuple(lst)}")
#con.commit()
x = cur.execute("SELECT * FROM book")

for i in x:
    print(i)
