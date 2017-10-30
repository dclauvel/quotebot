#!/usr/bin/env python
 
import tweepy, time, sys
 
tweets = 'tweets.txt'

 
CONSUMER_KEY = '0AzowIioWSCd8Vi1gM4ghFn9p'
CONSUMER_SECRET = 'yh7JYmZptDeWs2Ivg7SlSZ0QA3bvI9iLENtGM15PxfoApcKskd'
ACCESS_KEY = '925124098627440640-Wx5xqEzfPMOLxG9XttcSOmsFSOohyvq'
ACCESS_SECRET = 'tMsNz5CgeeW51IFqoGb0eNrWxSvilo6J3wt6XGyJCasEP'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(tweets,'r')
f=filename.readlines()
filename.close()
 
for tweet in f:
    api.update_status(tweet)
    time.sleep(900)