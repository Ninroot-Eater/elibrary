import csv
from app import app
from sqlalchemy.orm import Session
from models import setup_db, Book
from sqlalchemy import create_engine


def add_data(csv_file):
    x = setup_db(app)
    engine = create_engine(x)
    session = Session(engine)
    r = csv.reader(open(csv_file,"r",encoding="utf-8"))
    lst = [i for i in r]

    for i in lst:
        temp = Book(title=i[0],author=i[1],blink=i[2],btype=i[3],plink="#",des=i[5])
        session.add(temp)
        session.commit()
        print(temp)
add_data("blist.csv")