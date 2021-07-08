import csv
import os
from sqlalchemy import Column, String, Integer, create_engine, Boolean
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy.sql.operators import op

db = SQLAlchemy()



def setup_db(app):
    database_name ='elib'
    default_database_path= "postgresql://{}:{}@{}/{}".format('postgres', 'THU11!!%THEE', 'localhost:5432', database_name)
    database_path = os.getenv('DATABASE_URL', default_database_path)

    
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    return database_path


    


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()



class Book(db.Model):

    bid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    blink = db.Column(db.String)
    plink = db.Column(db.String)
    btype = db.Column(db.String)
    level = db.Column(db.String)
    des = db.Column(db.String)

    def __repr__(self):
        return f"<id {self.bid}>"


def add_data(csv_file):
    x = setup_db()
    engine = create_engine(x)
    session = Session(engine)
    r = csv.reader(open(csv_file,"r",encoding="utf-8"))
    lst = [i for i in r]

    for i in lst:
        print(i)