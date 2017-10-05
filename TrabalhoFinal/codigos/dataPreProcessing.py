#coding=utf-8
import nltk.data
from nltk.tokenize import word_tokenize

tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')

tweet = 'Alguien amable que me sugiera qué leer sobre #Cataluña? Gracias! 😊.'
#tweet=tweet.replace('#','')

print(tokenizer.tokenize(tweet))

