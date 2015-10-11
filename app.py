
from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
@app.route("/home")
def about():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0',port=8000)
