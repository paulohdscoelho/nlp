#coding=utf-8

from nltk.tag import UnigramTagger
from nltk.tag import BigramTagger
from nltk import tokenize
from nltk.corpus import mac_morpho

def train(tagger, sent):
	resultado = []
	for word, tag in tagger.tag(sent):
		print(word, ' -> ', tag)
	#return resultado

dados_treino = mac_morpho.tagged_sents()[:1000]

dicTags = {}

for e in dados_treino:
	print('Dado: ',e)
	#dicTags[e[1]] = []

print(dicTags)


print(dados_treino)
#tagged_text =  open('macmorpho-test.txt').read()
#tokens = tokenize.sent_tokenize(tagged_text)

print("treinando")
tagger = UnigramTagger(dados_treino)

tagger2 = BigramTagger(dados_treino, backoff=tagger)

print("terminou")
print(tagger2.evaluate(mac_morpho.tagged_sents()[1000:1200]))



'''teste = open("macmorpho-test.txt").read()
teste_tokens = tokenize.word_tokenize(teste)

print("teste")
teste_teinado = train(tagger,teste_tokens)


#for e in teste_teinado:
	#print e

#print(tagger.tag(teste_tokens))

#print(tokens)'''