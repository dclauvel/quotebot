#!/usr/bin/env python
 
import tweepy, time, sys, os
 
tweets = 'tweets.txt'

CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_KEY = os.environ["ACCESS_KEY"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(tweets,'r')
f=filename.readlines()
filename.close()
 
for tweet in f:
	try:
    	api.update_status(tweet)
    	time.sleep(900)
    except tweepy.TweepError:
    	pass