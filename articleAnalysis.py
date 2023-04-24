"""
This file uses the textblot and newspaper libraries to analyze the sentiment of a news article
given it's url in the command line.
"""
from textblob import TextBlob
from newspaper import Article
import sys

input = sys.argv
# usage statement
if len(input) != 2:
    print("Needs url of an article to run.")
    exit()

url = input[1]
article = Article(url)

article.download()  # get article into script
article.parse()     # removes html / makes readable
article.nlp()       # preps it for nlp

text = article.text  # gives all text in article (string)
summary = article.summary   # summarizes article contents (string)

blob = TextBlob(summary)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)