from flask import Flask, render_template, redirect
import pymongo
import scrape_mars
from flask_pymongo import PyMongo 
app = Flask(__name__)

@app.route("/")
def index():

@app.route("/recommendations")
def book_recommend():


    return redirect("/")
    


if __name__ == "__main__":
    app.run(debug=True)