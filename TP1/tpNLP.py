#coding=utf-8

from gensim.models.keyedvectors import KeyedVectors
from gensim.models import word2vec
import numpy as np
import sys
import math

'''
Primeiro, rodar essa linha no diretório do word2vec em C:
./word2vec -train ../AChristmasCarol-CharlesDickens.txt -output ../Vectors.bin -size 100 -window 8 -negative 25 -hs 0 -sample 1e-4 -threads 20 -binary 1 -iter 15
Após salvar o binário, carregar no script Python e calcular as distâncias

'''

def distancia(matrizA, matrizB):

	somadorFinal = 0

	for i in range(len(matrizA[0])):
		somaRow = 0
		for j in range(len(matrizA[1])):
			somaRow += pow(matrizA[i][j] - matrizB[i][j],2)
		somadorFinal += somaRow
	return math.sqrt(somadorFinal)


def geraMatriz(word_vectors):
	setWords = []
	for key in word_vectors.vocab:
		setWords.append(key)
	
	distanceMatrix = []
	for row in setWords:
		arrayDistance = []
		for col in setWords:
			try:
				similarity = word_vectors.similarity(str(row), str(col))
				arrayDistance.append(similarity)
			except KeyError:
				continue
		distanceMatrix.append(arrayDistance)
	return distanceMatrix


word_vectors = KeyedVectors.load_word2vec_format('Vectors.bin', binary=True)  # C binary format

word_vectors2 = KeyedVectors.load_word2vec_format('Vectors2.bin', binary=True)  # C binary format

matrizLivro1 = geraMatriz(word_vectors)
matrizLivro2 = geraMatriz(word_vectors2)

print distancia(matrizLivro1,matrizLivro2)
