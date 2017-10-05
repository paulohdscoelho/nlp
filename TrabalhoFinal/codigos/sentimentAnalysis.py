#coding=utf-8

import indicoio
import numpy as np

indicoio.config.api_key = '3bed82d6a725495d0adee82b70b3a6f1'


# batch example

for tweet in matrizTweets:

	sentiment = indicoio.sentiment(tweet,language='spanish')