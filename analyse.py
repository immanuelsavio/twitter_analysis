#This file is used to analyse twitter feeds using textblob and classify into positive, negative or zero.
from textblob import TextBlob
import tweepy

consumer_key = '<Enter Key>'
consumer_secret = '<Enter Key>  '

access_token = '<Enter Key>'
access_token_secret = '<Enter Key>'

authenticate = tweepy.OAuthHandler(consumer_key, consumer_secret)
authenticate.set_access_token(access_token,access_token_secret)

api = tweepy.API(authenticate)
search_tweets = api.search('KCR')

for tweet in search_tweets:
    print(tweet.text)

    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)