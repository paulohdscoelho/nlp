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

while True:
	bin1 = input("Digite o primeiro livro ") 
	#bin2 = raw_input("Digite o segundo livro") 
	with open("../analisesTP.dat",'a') as saida:
		print("iniciando")
		word_vectors1 = KeyedVectors.load_word2vec_format(bin1+'.bin', binary=True)  # C binary format
		#word_vectors2 = KeyedVectors.load_word2vec_format(bin2+'.bin', binary=True)  # C binary format

		dictWords = word_vectors1.vocab
		keysA = set(dictWords.keys())
		for key in keysA:
			
			saida.write(key+'\t')
			saida.write(str(dictWords[key])+'\n')
		
		#keysB = set(word_vectors2.vocab.keys())

		#intersection = keysA & keysB

		#matrizLivro1 = geraMatriz(intersection,word_vectors1)
		#matrizLivro2 = geraMatriz(intersection,word_vectors2)

		#saida.write('=============================================================\n')
		#saida.write("Distância entre os livros " + bin1.replace('.bin','') + " vs " + bin2.replace('.bin','')+':\n')
		#saida.write("{0:.2f}\n".format(round(distanciaPadrao(matrizLivro1,matrizLivro2),2)))
		#print("Pronto")

