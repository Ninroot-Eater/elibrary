from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = "verysecretkey"



@app.route("/")
def home():
    con = sql.connect("data.db")
    cur = con.cursor()
    y = cur.execute("SELECT * FROM book")
    x = [i for i in y]
    return render_template("index.html", x = x[1:4])


if __name__ == "__main__":
    app.run(debug=True)

