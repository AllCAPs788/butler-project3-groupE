from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/recommendations")
def book_recommend():
    return render_template("pandas.html")

def raw_data():
    return render_template("raw_data.html")
    return redirect("/")
    

    

if __name__ == "__main__":
    app.run(debug=True)