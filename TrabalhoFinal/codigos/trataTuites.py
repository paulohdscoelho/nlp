#coding=utf-8
import sys
import json
import re as re
from datetime import datetime
import sys

#sed -f <(sed 's/.*/s|\\\<&\\\>||g/' stopwords.txt) tweetsCatalunhaPassados.txt > tweetsCatalunha.txt


#with open('scraperCatalunha.json','r') as textEntrada:
#    json_data = textEntrada.readline()
    
#json_data = json.loads(json_data)

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)


with open(sys.argv[1]) as entrada:
	lines = [line.split('\t') for line in entrada]
	for tweet in lines:
		text = tweet[1]
		weekday = tweet[0].split(' ')[0]
		with open('tweetsCatalunha'+str(weekday)+'.txt','a') as saida:
			if(' RT ' not in text):				
				if 'http' in text:
					text = text.split('http')[0]
				
				if '.twitter.com' in text:
					text = text.split('.twitter.com')[0]
				
				text = re.sub(r"(?:\#|\@|http[_,s]?\://)\S+", "", text)
				text = emoji_pattern.sub(r'', text) #no Emoji
				text = text.replace('pic','').replace('Twitter','').replace('\n',' ').replace('\r',' ')
				print(str(text))
				saida.write(str(text)+'\n')
