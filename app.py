from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/love")
def love():
    return render_template("love.html")

@app.route("/think_again")
def think_again():
    return render_template("think_again.html")

@app.route("/why")
def why():
    return render_template("why.html")

@app.route("/final_love")
def final_love():
    return render_template("love.html")

if __name__ == "__main__":
    app.run(debug=True)
