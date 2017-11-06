#coding=utf-8
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy.utils import import_simplejson
import json
from geopy.geocoders import Nominatim

consumer_key = 'DEmDJdwDhXDHbZcsz91eBT9YA'
consumer_secret = 'LfeYIwQYvrjuyvpGGXd1Mx4Q9aywCdupY2tAq14dDp0Z3mF5ka'
access_token = '1058812796-wjKPbjL2pJrK82cAn9HSQVhAqxV7fJrTuDRS76f'
access_secret = 'MXDo6I0CeJf9kVBB6PwNwqPRj9RsWSjV9Wx4l4S4GKiNL'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
geolocator = Nominatim()

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('dadosTwitterCat.txt','a') as saida:
                json_data = json.loads(data)
       
                text = json_data['text'].replace('\n'," ")
                print(text)
                saida.write(text+'\n')
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=[u'catalunya referendum referéndum referendo', u'cataluña referéndum referendo referendum', u'catalonia referendo referendum referéndum', u'catalunha referendo referendum referéndum'])
