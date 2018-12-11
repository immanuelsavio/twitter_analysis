#This file is used to analyse twitter feeds using textblob and classify into positive, negative or zero.
import textblob
import tweepy

consumer_key = 'Consumer Key'
consumer_secret = 'Consumer Secret Key'

access_token = 'Access Token'
access_token_secret = 'Access Token Secret'

authenticate = tweepy.OAuthHandler(consumer_key, consumer_secret)
authenticate.set_access_token(access_token,access_token_secret)

API = tweepy.API(authenticate)