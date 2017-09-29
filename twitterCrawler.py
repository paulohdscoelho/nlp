#coding=utf-8
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy.utils import import_simplejson
import json
from nltk.tokenize import word_tokenize
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
            with open('dadosTwitter.txt','a') as saida:                
                json_data = json.loads(data)

                if json_data['geo'] != None:
                    if json_data['geo']['coordinates'] != None:
                        coordinate = json_data['geo']['coordinates']                    
                        coordinate = str(coordinate[0]) + ', ' + str(coordinate[1])
                        location = geolocator.reverse(coordinate)
                        array = location.address.encode('utf-8').split(',')
                        if array[-1].strip() == 'United States of America':

                            text = hora = json_data['created_at'] +'\t' + json_data['text'].encode('utf-8') + '\t' + str(location.address).encode('utf-8').strip()
                            print text
                            saida.write(text+'\n')
            return True
        except BaseException as e:   
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['I\'m at Swarmapp com'])
