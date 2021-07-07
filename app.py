from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = "verysecretkey"



@app.route("/")
def home():
    con = sql.connect("data.db")
    cur = con.cursor()
    x = cur.execute("SELECT * FROM book")
    for i in x:
        print(i)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

