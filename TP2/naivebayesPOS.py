#coding=utf-8
import nltk
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
dados_teste = mac_morpho.tagged_sents()[1000:1200]
tagSet = set(['NPROP', 'PREP+PRO-KS', 'KS', 'PREP+PROADJ', 'PREP', 'PREP+PROPESS', 'NUM', 'KC', 'PROADJ', 'PREP+ART', 'IN', 'ART', 'PREP+PROSUB', 'PROPESS', 'PCP', 'ADV-KS', 'PRO-KS', 'PDEN', 'PU', 'PROSUB', 'ADV', 'V', 'PREP+ADV', 'N', 'CUR', 'ADJ'])

print("Tag\tAccuracy with Unigram\tAccuracy with Bigram")

for tag in tagSet:
	
	tag_train = nltk.DefaultTagger(tag)
	tagger = UnigramTagger(dados_treino,backoff=tag_train)	
	accuacyUnigram = tagger.evaluate(dados_teste)
	tagger2 = BigramTagger(dados_treino, backoff=tagger)	
	accuacyBigram = tagger2.evaluate(dados_teste)

	print(tag,'\t',accuacyUnigram,'\t',accuacyBigram)

'''teste = open("macmorpho-test.txt").read()
teste_tokens = tokenize.word_tokenize(teste)

print("teste")
teste_teinado = train(tagger,teste_tokens)


#for e in teste_teinado:
	#print e

#print(tagger.tag(teste_tokens))

#print(tokens)'''