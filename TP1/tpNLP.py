#coding=utf-8

from gensim.models.keyedvectors import KeyedVectors
from gensim.models import word2vec
import numpy as np
import sys
import math 
from math import*
from scipy import stats

def distanciaPadrao(matrizA, matrizB):
	somadorFinal = 0
	for i in range(len(matrizA[0])):
		somaRow = 0
		for j in range(len(matrizA[1])):
			somaRow += pow(matrizA[i][j] - matrizB[i][j],2)
		somadorFinal += somaRow
	return math.sqrt(somadorFinal)

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


bin1 = sys.argv[1]
bin2 = sys.argv[2]

word_vectors1 = KeyedVectors.load_word2vec_format(bin1, binary=True)  # C binary format
word_vectors2 = KeyedVectors.load_word2vec_format(bin2, binary=True)  # C binary format

keysA = set(word_vectors1.vocab.keys())
keysB = set(word_vectors2.vocab.keys())

intersection = keysA & keysB

matrizLivro1 = geraMatriz(intersection,word_vectors1)
matrizLivro2 = geraMatriz(intersection,word_vectors2)

print("{0:.2f}".format(round(distanciaPadrao(matrizLivro1,matrizLivro2),2)))

