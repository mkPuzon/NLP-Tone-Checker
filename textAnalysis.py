"""
This file 
"""
from textblob import TextBlob
import sys

user_input = sys.argv
if len(user_input) != 2:
    print("Need a txt file to read")
    exit()

with open(user_input[1], 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)