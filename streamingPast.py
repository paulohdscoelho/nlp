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

api = tweepy.API(auth)


 with open('tweetsPast.txt','a') as saida:
for tweet in tweepy.Cursor(api.search,q=[u'catalunya referendum referéndum referendo', u'cataluña referéndum referendo referendum', u'catalonia referendo referendum referéndum', u'catalunha referendo referendum referéndum'],count=100,\
                           lang="en",\
                           since_id=2017-09-29).items():
    json_data = json.loads(tweet)
    if json_data['geo'] != None:
        if json_data['geo']['coordinates'] != None:
            coordinate = json_data['geo']['coordinates']            
            coordinate = str(coordinate[0]) + ', ' + str(coordinate[1])
            location = geolocator.reverse(coordinate)
            array = location.address.encode('utf-8').split(',')
            text = hora = json_data['created_at'] +'\t' + json_data['text'].encode('utf-8') + '\t' + str(location.address).encode('utf-8').strip()
            print text.encode('utf-8')
            saida.write(text.encode('utf-8')+'\n')
