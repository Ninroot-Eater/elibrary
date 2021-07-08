from flask import Flask, render_template
from sqlalchemy.engine import create_engine
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

x = Book(bid=1,title="The Hobbit",author="J.R.R. Tolkein", blink="https://blink", plink="https://plink",
        btype="Fiction",level="IELTS",des="A very good book. Must read. hahahah")
#session.add(x)
#session.commit()
@app.route("/")
def home():
    x = session.get(Book,1)
    return render_template("index.html", x = x)


if __name__ == "__main__":
    app.run(debug=True)

