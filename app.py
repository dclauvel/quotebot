#!/usr/bin/env python
 
import tweepy, time, sys, os, logging, json
 
logger = logging.getLogger('stickybot')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
logger.addHandler(ch)


tweets = 'steinbeck.txt'

CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_KEY = os.environ["ACCESS_KEY"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]

try:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    logger.debug("Successfull auth")
except tweepy.TweepError as e:
    logger.debug("Failed to auth " + e.response.text)

filename=open(tweets,'r')
f=filename.readlines()
filename.close()

for l in f:
    try:
        j = json.load(l)
        tweet = j['field1'][0]
        api.update_status(tweet)
        logger.debug("Tweeted " + tweet)
        time.sleep(900)
        logger.debug("Finished sleeping")
    except tweepy.TweepError:
        pass