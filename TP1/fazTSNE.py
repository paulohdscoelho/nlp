#coding=utf-8
from sklearn.manifold import TSNE
import numpy as np
from random import randint
import sys
import matplotlib.pyplot as plt, mpld3
import matplotlib.cm as cm
import matplotlib.patches as mpatches


def graficoTSNE(fig,ax,arquivo,color):

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

  with open('MatrizTSNEPaises/TSNE_'+arquivo+'.dat') as textFile:
    vis_data = np.loadtxt(textFile,usecols=range(0,3),delimiter ='\t',dtype='float')

  vis_x = vis_data[:, 0] #coordenada X
  vis_y = vis_data[:, 1] #coordenada Y
 
  scale = 10.0 

  scatter = ax.scatter(vis_x, vis_y, c=color, cmap='gray',s=scale, label=arquivo,
               alpha=0.6, edgecolors='none')

  ax.legend()
  ax.grid(True)

  #AQUI VOCÊ TEM QUE CRIAR UM VETOR COM OS LABELS!!!! 
  #TIPO, CADA LINHA DA SUA MATRIZ ORIGINAL REPRESENTA UMA COISA, ENTÃO VOCÊ VAI DANDO APEND EM labels, PRA ADICIONAR O "NOME" DE CADA LINHA
  #ISSO VAI APARECER NO TOOLTIP DA PÁGINA DO TSNE

  labels = []
  for i in range(0,vis_data.shape[0]):
    labels.append(arquivo)

  tooltip = mpld3.plugins.PointHTMLTooltip(scatter, labels, voffset=-20, hoffset=10, css=css)
  mpld3.plugins.connect(fig, tooltip)
  
  del scatter,tooltip

def main():
  
  arrayPaises = []
  
  try:
    sys.argv[1]
  except IndexError:
    print('!!ERRO!!\nVoce deve informar ao menos um país para cálculo na chamada do programa\n!!ERRO!!')
    exit()
  print("Iniciando...")
  for itens in sys.argv[1:]:
    arrayPaises.append(itens)

  x = np.arange(len(arrayPaises))
  ys = [i+x+(i*x)**2 for i in range(len(arrayPaises))]

  colors = cm.rainbow(np.linspace(0, 1, len(ys)))
  fig, ax = plt.subplots(subplot_kw=dict(axisbg='#EEEEEE'))

  fig.set_figheight(12)
  fig.set_figwidth(16)

  ax.set_title("Grafico de Dispersao de Culture to zScores", size=20)

  for pais,color in zip(sorted(arrayPaises),colors):
    print ("Calculando  "+str(pais))    
    graficoTSNE(fig, ax,pais,color)
  
  mpld3.save_html(fig, "saida/TSNE_cultureToZScores.html")
  fig.savefig(str('saida/TSNE_cultureToZScores.png'))
  mpld3.show()

  plt.close(fig)
  print("Pronto!")

main()