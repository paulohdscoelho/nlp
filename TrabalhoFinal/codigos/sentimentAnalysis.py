#coding=utf-8

import indicoio
import numpy as np
import sys

indicoio.config.api_key = '8c4677945e91b7437e74356d854d3c57'


with open(sys.argv[1],encoding = 'utf-8') as textEntrada:
	for tweet in textEntrada:
		try:
			sentiment = indicoio.sentiment(tweet,language='spanish')
			if sentiment > 0.5:
				print("pos\t",tweet)
			if sentiment < 0.5:
				print("neg\t",tweet)
			if sentiment == 0.5:
				print("mid\t",tweet)

		except Exception as e:
			print(e)
			pass