#coding=utf-8
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy.utils import import_simplejson
import json
from geopy.geocoders import Nominatim
import time
import sys
 


consumer_key = 'DEmDJdwDhXDHbZcsz91eBT9YA'
consumer_secret = 'LfeYIwQYvrjuyvpGGXd1Mx4Q9aywCdupY2tAq14dDp0Z3mF5ka'
access_token = '1058812796-wjKPbjL2pJrK82cAn9HSQVhAqxV7fJrTuDRS76f'
access_secret = 'MXDo6I0CeJf9kVBB6PwNwqPRj9RsWSjV9Wx4l4S4GKiNL'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

geolocator = Nominatim()

api = tweepy.API(auth)

cursor = tweepy.Cursor(api.search,q=((u'cataluña' or 'calatayud' or 'cataluna' or 'catalonia' or'catalunha') and('referendum' or'referendo' or u'referéndum')), since='2017-10-24',until='2017-10-31').items()

while True:
    try:
        tweet = cursor.next()
        with open('tweetsPast-Catalunia.txt','a') as saida:
            if(tweet.retweeted == False and tweet.lang == u'en' and 'RT @' not in tweet.text and '@' not in tweet.text and ' RT ' not in tweet.text and 'https' not in tweet.text):
                print(str(tweet.text))
                saida.write(str(tweet.text.replace('\n',' ').replace('\t',' '))+'\n')
            del tweet
    except BaseException as e:
        print(e)
        time.sleep(60 * 15)
        continue

