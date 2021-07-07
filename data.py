import sqlite3 as sql
import csv

con = sql.connect("data.db")
cur = con.cursor()

def from_csv():
    with open("blist.csv","r",encoding="utf-8") as f:
        x = csv.reader(f)
        x = [i for i in x]
        c = 3
        for i in x:
            i.append("None")
            i.insert(0,c)
            print(i)
            cur.execute(f"INSERT INTO book VALUES {tuple(i)}")
            con.commit()
            print("added")
            c+=1


