# Be a Reading Machine

![book stacks](https://raw.githubusercontent.com/AllCAPs788/butler-project3-groupE/master/assets/images/book_stacks_1.jpg)

We want to recommend books to users based on their choice of book title. To do this we will use machine learning algorithms to analyze text to find the most similar books to the user's choice. 

What are we using? Scikit Learn, Pandas, Postgres SQL, HTML/CSS, Flask, Jinja, Google Slides (presentation)

What are we trying to predict? 

Based on the user's choice of book title, we will provide recommendations using a content-based system that uses title, author, publisher, and categories (genres) to let them expand on their tastes. 

## Our Model

For our recommender system, we use the following book attributes:
* title
* author
* publisher
* category (genre)

## Data

If you would like to see our full dataset, you can find it [**here**](../Data/cleaned_books.csv). We then load it onto our Postgres SQL database [insert link]

That data was originally pulled from two separate datasets off Kaggle:
* https://www.kaggle.com/dylanjcastillo/7k-books-with-metadata 
* https://www.kaggle.com/jealousleopard/goodreadsbooks 

We then combined that data into the CSV linked above. From there, we cleaned the data in our Jupyter [**Notebook**](https://github.com/AllCAPs788/butler-project3-groupE/blob/master/Data/data_cleaning.ipynb). 


## Final Result

As you can see, the final result is that your choice in book title will allow our model to return recommendations for you. 






