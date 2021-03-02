from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo 
app = Flask(__name__)

# rds_connection_string = "postgres:postgres@localhost:5432/books_db"
# engine = create_engine(f'postgresql://{rds_connection_string}')

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/pandas")
def pandas():
    return render_template("pandas.html")
@app.route("/data")
def raw_data():
    return render_template("raw_data.html")
@app.route("/api")
def api():
    return render_template("api.html")
@app.route("/documents")    
def documents():
    return render_template("documents.html")    
    
    
    
    

    

if __name__ == "__main__":
    app.run(debug=True)