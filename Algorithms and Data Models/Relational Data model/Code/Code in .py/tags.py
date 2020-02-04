import pandas as pd
import numpy as np 
from wordcloud import WordCloud, STOPWORDS , ImageColorGenerator
import matplotlib.pyplot as plt

tagsCSV = pd.read_csv("tags.csv")
moviesCSV = pd.read_csv("movies.csv")

popularTags = pd.merge(moviesCSV, tagsCSV, on='movieId', how='inner')
popularTags.timestamp = pd.to_datetime(popularTags.timestamp, infer_datetime_format=True)
popularTags.timestamp = popularTags.timestamp.dt.year
popularTags.sort_values(by='movieId', inplace=True)
print ("Number of  Null values: ", max(popularTags.isnull().sum()))
popularTags.head()

# convert to list
popularTags['genres'] = popularTags.genres.str.split('|')
# convert list of pd.Series then stack it
popularTags = (popularTags.set_index(['movieId','title','userId','tag','timestamp'])['genres']
 .apply(pd.Series)
 .stack()
 .reset_index()
 .drop('level_5', axis=1)
 .rename(columns={0:'genres'}))
popularTags.head()

popularTags[popularTags.genres == 'Drama']

n=20
Drama = []
Drama = popularTags.tag.value_counts()[:n].index.tolist()
#print(Adventure)

stopwords = set(STOPWORDS)

def show_wordcloud(data, title = None):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_font_size=40, 
        scale=3,
).generate(str(data))

    fig = plt.figure(1, figsize=(10, 15))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=40)
        #fig.subplots_adjust(top=2.3)
    plt.title('Most Used Words for most popular genre drama')    
    plt.imshow(wordcloud)
    plt.show()

show_wordcloud(Drama)

popularTags[popularTags.genres == 'Comedy']

n=20
Comedy = []
Comedy = popularTags.tag.value_counts()[:n].index.tolist()

stopwords = set(STOPWORDS)

def show_wordcloud(data, title = None):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_font_size=40, 
        scale=3,
).generate(str(data))

    fig = plt.figure(1, figsize=(10, 15))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=40)
        #fig.subplots_adjust(top=2.3)
    plt.title('Most Used Words for 2nd most popular genre Comedy')    
    plt.imshow(wordcloud)
    plt.show()

show_wordcloud(Drama)

