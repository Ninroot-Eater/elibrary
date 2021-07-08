from re import A
import re
from flask import Flask, render_template, request
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



@app.route("/", methods=["GET","POST"])
def home():
    x = Book.query.all()
    
    return render_template("index.html", x = x)

@app.route("/search", methods=["POST"])
def search():
    if request.method == "POST":
        q = request.form.get("search")
        q = q.lower()
        x = Book.query.filter(Book.tags.like(f"%{q}%")).all()
        
        x = Book.query.filter(Book.title.like(f"%{q}%")).all()
        lst = []
    
        for i in x:
            if q in i.title.lower():
                lst.append([i.title,i.author,i.bid,i.title.lower().index(q)])
    
        
    
        lst.sort(key=lambda x:x[2])
        
        return render_template("results.html", x = lst)

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

