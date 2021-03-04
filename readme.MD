# Be a Reading Machine

![book stacks](https://raw.githubusercontent.com/AllCAPs788/butler-project3-groupE/master/assets/images/book_stacks_1.jpg)

We want to know which books will be recommended to users based on their choices in titles. To do this we will use a text-based algorithm that works off parameters listed below. 

what are we using? Sci-kit, Pandas, Tableau, Google Slides (presentation for investors/CEOs), Postgres SQL

What are we trying to predict? 

Based on your choices, we will provide you recommendations based on title, author, publisher, and categories (genres) to let you expand on your tastes. 

## Our Algorithm

For our recommendation algorith, we use the following input from user choices:
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

## Tableau   

Before you make your choices, we have visualizations of the trends that exist in our starting data. These visualizaations correspond to the four factors that affect the recommendations returned based on your choices. 

## Final Result

As you can see, the final result is that your choices in titles will allow our algorithm to return recommendations for you. 






