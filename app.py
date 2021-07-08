from re import A
import re
from flask import Flask, render_template
from sqlalchemy.engine import create_engine
from werkzeug.utils import redirect
from models import setup_db, db_drop_and_create_all, db, Book
from flask_migrate import Migrate
from sqlalchemy.orm import Session, session


app = Flask(__name__)
app.config['SECRET_KEY'] = "verysecretkey"
x = setup_db(app)


migrate = Migrate(app,db)
db.create_all()


engine = create_engine(x)
session = Session(engine)



@app.route("/")
def home():
    x = Book.query.all()
    
    return render_template("index.html", x = x)


def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
@app.route("/detail/<int:bid>")
def detail(bid):
    if is_int(bid):
        x = Book.query.get(bid)
        return render_template("detail.html",x=x)
    return redirect(home)


if __name__ == "__main__":
    app.run(debug=True)

