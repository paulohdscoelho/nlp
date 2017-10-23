#coding=utf-8

from gensim.models.keyedvectors import KeyedVectors
from gensim.models import word2vec
import numpy as np
import sys
import math 
from math import*

from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt, mpld3
import matplotlib.cm as cm


def distanciaPadrao(matrizA, matrizB):
	somadorFinal = 0
	for i in range(len(matrizA[0])):
		somaRow = 0
		for j in range(len(matrizA[1])):
			somaRow += pow(matrizA[i][j] - matrizB[i][j],2)
		somadorFinal += somaRow
	return math.sqrt(somadorFinal)

def geraMatriz(word_vectors):
	distanceMatrix = []
	for row in word_vectors.vocab:
		arrayDistance = []
		for col in word_vectors.vocab:
			try:				
				similarity = word_vectors.similarity(str(row), str(col))
				arrayDistance.append(similarity)
			except KeyError:
				continue
		distanceMatrix.append(arrayDistance)
	return distanceMatrix


def graficoTSNE(fig,ax,arquivo,color):

	word_vectors = KeyedVectors.load_word2vec_format(str(arquivo)+'.bin', binary=True)  # C binary format
	labels = list(word_vectors.vocab.keys())

	#matriz =[]
	#for key in word_vectors.vocab:
	#	matriz.append(word_vectors[key])

	matriz = geraMatriz(word_vectors)

	vis_data = TSNE(init='pca',perplexity=50.0).fit_transform(matriz)

	css = """
	text.mpld3-text, div.mpld3-tooltip {
	    font-family: Arial, Helvetica, sans-serif;
	    font-weight: bold;
	    color: black;
	    opacity: 1.0;
	    padding: 2px;
	    border: 0px;
	}
	"""

	vis_x = vis_data[:, 0] #coordenada X
	vis_y = vis_data[:, 1] #coordenada Y

	scale = 30.0 
	scatter = ax.scatter(vis_x, vis_y, c=color, cmap='gray',s=scale, label=arquivo,
	           alpha=0.9, edgecolors='none',encoding='utf-8')

	ax.legend()
	ax.grid(True)

	#AQUI VOCÊ TEM QUE CRIAR UM VETOR COM OS LABELS!!!! 
	#TIPO, CADA LINHA DA SUA MATRIZ ORIGINAL REPRESENTA UMA COISA, ENTÃO VOCÊ VAI DANDO APEND EM labels, PRA ADICIONAR O "NOME" DE CADA LINHA
	#ISSO VAI APARECER NO TOOLTIP DA PÁGINA DO TSNE
	tooltip = mpld3.plugins.PointHTMLTooltip(scatter, labels, voffset=-20, hoffset=10, css=css)
	mpld3.plugins.connect(fig, tooltip)

  	del scatter,tooltip


def main():
  
  arrayLivros = []
  
  try:
    sys.argv[1]
  except IndexError:
    print('!!ERRO!!\nVoce deve informar ao menos um país para cálculo na chamada do programa\n!!ERRO!!')
    exit()
  print("Iniciando...")
  for itens in sys.argv[1:]:
    arrayLivros.append(itens.replace('.bin',''))

  x = np.arange(len(arrayLivros))
  ys = [i+x+(i*x)**2 for i in range(len(arrayLivros))]

  colors = cm.rainbow(np.linspace(0, 1, len(ys)))
  fig, ax = plt.subplots(subplot_kw=dict(axisbg='#EEEEEE'))

  fig.set_figheight(12)
  fig.set_figwidth(16)

  ax.set_title("Grafico de Dispersao de word2vec", size=20)

  for livro,color in zip(sorted(arrayLivros),colors):
    print ("Calculando  "+str(livro))    
    graficoTSNE(fig, ax,livro,color)
 
  nomeSaida = '-'.join(arrayLivros)


  fig.savefig(str('../saidaTP/TSNE_'+nomeSaida+'.png'))
  mpld3.show()

  plt.close(fig)
  print("Pronto!")

main()