import csv
import os
from sqlalchemy import Column, String, Integer, create_engine, Boolean
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.operators import op

db = SQLAlchemy()



def setup_db(app):
    database_name ='elib'
    default_database_path= "postgresql://stefdqcvulajbn:6e372d2f92d2e275d28afc2274739368bd08ed50743accbaae4281b00a557f01@ec2-34-202-54-225.compute-1.amazonaws.com:5432/d5il4lge2reh4p".format('postgres', 'THU11!!%THEE', 'localhost:5432', database_name)
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
        return f"<id {self.bid} {self.title}>"


