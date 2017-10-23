#coding=utf-8

from gensim.models.keyedvectors import KeyedVectors
from gensim.models import word2vec
import numpy as np
import sys
import math 
from math import*
from scipy import stats


def geraMatriz(intersection,word_vectors):
	distanceMatrix = []
	for row in intersection:
		arrayDistance = []
		for col in intersection:
			try:				
				similarity = word_vectors.similarity(str(row), str(col))
				arrayDistance.append(similarity)
			except KeyError:
				continue
		distanceMatrix.append(arrayDistance)
	return distanceMatrix


word_vectors = KeyedVectors.load_word2vec_format('tweetsCatalunha.bin', binary=True)  # C binary format

for word in word_vectors.vocab:
	print(str(word) + ' - ' + str(word_vectors[word]))

