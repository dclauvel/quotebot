#!/usr/bin/env python
 
import tweepy, time, sys
 
tweets = 'tweets.txt'

 
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(tweets,'r')
f=filename.readlines()
filename.close()
 
for tweet in f:
    api.update_status(tweet)
    time.sleep(900)