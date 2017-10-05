#coding=utf-8
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy.utils import import_simplejson
import json
from twitterscraper import query_tweets


# All tweets matching either Trump or Clinton will be returned. You will get at
# least 10 results within the minimal possible time/number of requests
for tweet in query_tweets("cataluña OR catalonia"):
    print(tweet.user.encode('utf-8'))


