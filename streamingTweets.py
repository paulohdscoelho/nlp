#coding=utf-8
import sys
import json

with open('scraperCatalunha.json','r') as textEntrada:
    json_data = textEntrada.readline()
    
json_data = json.loads(json_data)

for tweet in json_data:
    with open('tweetsCatalunhaPassados.txt','a') as saida:
        if('RT @' not in tweet['text'] and ' @' not in tweet['text'] and 'https' not in tweet['text'] and 'http' not in tweet['text']):
            text = tweet['timestamp'] +'\t' + str(tweet['text']) + '\t'
            print(str(text))
            saida.write(str(text)+'\n')

    
    
'''for tweet in json_data:
with open('tweetsCatalunhaPassados.txt','a') as saida:
if(tweet['retweeted'] == False and 'RT @' not in tweet['text'] and ' @' not in tweet['text'] and 'https' not in tweet['text']):

if tweet['user'][u'location'] != None:
text = str(tweet['created_at']) +'\t' + tweet['text'] + '\t' + tweet['user'][u'location']
else:
text = tweet['created_at'] +'\t' + str(tweet['text']) + '\t' + 'None'
print(str(text))
saida.write(str(text)+'\n')'''
