from flask import Flask, render_template, redirect, jsonify, request
import pymongo
from flask_pymongo import PyMongo 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel


app = Flask(__name__)

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
    
@app.route('/results', methods=['POST'])
def results():

    #create engine to connect to SQL database
    rds_connection_string = "postgres:postgres@localhost:5432/books_db"
    engine = create_engine(f'postgresql://{rds_connection_string}')
    #connect to SQL database
    connection = engine.connect()

    # creat dataframe from database
    df = pd.read_sql('SELECT index, title, authors, publisher, \
        categories, thumbnail \
        FROM books;' , connection)
    
    # combine text columns to analyze into one
    df['all'] = df['title'] + df['authors'] + df['publisher'] + df['categories']
    
    # set vectorizer as TFIDvectorizer from sklearn
    vectorizer = TfidfVectorizer(analyzer='word')

    # returns a matrix of the documents & TF-IDF calculations
    tfidf_all_content = vectorizer.fit_transform(df['all'])

    # create cosine similarity matrix
    cosine_similarity_all_content = linear_kernel(tfidf_all_content, tfidf_all_content)

    # create new dataframe with reset index
    books = df.reset_index(drop=True)

    # create a series of the indexes
    indices = pd.Series(books["title"].index)

    # get book title entered by the user
    user_title = request.form["booktitle"]
    
    # use user's book title to find index of that book
    input_array = books[books["title"] == user_title].index.values
    input_index = input_array[0]

    # function to get the most similar books
    def recommend(index, method):
        id = indices[index]
        similarity_scores = list(enumerate(method[id]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        similarity_scores = similarity_scores[1:11]
        books_index = [i[0] for i in similarity_scores]
        titles = books['title'].iloc[books_index]
        authors = books['authors'].iloc[books_index]
        a_zip = zip(titles, authors)
        data = list(a_zip)
        return data

    # pass the book index & cosine similarities to create list of recommended books
    book_list = recommend(input_index, cosine_similarity_all_content)
    #book_list_html = book_list.to_html()

    return render_template("pandas.html", book_text='Recommendations based on {}'.format(user_title), \
        results_table=book_list)    
    
        

if __name__ == "__main__":
    app.run(debug=True)