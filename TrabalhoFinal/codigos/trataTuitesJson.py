#coding=utf-8
import sys
import json
import re as re
from datetime import datetime

#sed -f <(sed 's/.*/s|\\\<&\\\>||g/' stopwords.txt) tweetsCatalunhaPassados.txt > tweetsCatalunha.txt


with open('scraperCatalunha.json','r') as textEntrada:
    json_data = textEntrada.readline()
    
json_data = json.loads(json_data)

with open('tweetsCatalunha.txt') as entrada:
	lines = [line.split('\t') for line in entrada]
	for rawTweet in json_data:
		text = rawTweet.text.strip().replace('\n',' ').replace('\r',' ')
		with open('tweetsCatalunhaComStW.txt','a') as saida:
			if(' RT @' not in text):				
				if 'http' in text:
					text = text.split('http')[0]				
				if '.twitter.com' in text:
					text = text.split('.twitter.com')[0]				
				text = re.sub(r"(?:\#|\@|http[_,s]?\://)\S+", "", text)
				text = text.replace('pic','').replace('Twitter','')
				print(str(text))
				saida.write(str(text)+'\n')
