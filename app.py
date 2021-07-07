from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "verysecretkey"

@app.route("/")
def home():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True)

