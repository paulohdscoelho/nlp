from nltk.tag import UnigramTagger
from nltk import tokenize

tagged_text =  open('macmorpho-train.txt').read()
tokens = tokenize.sent_tokenize(tagged_text)

#tagger = UnigramTagger()

#tagger.train(tokens)

#texto = 'O cachorro sábio sabia assobiar'

#texto_tokens = tokenize.word_tokenize(texto)

#print(tagger.tag(texto_tokens))

print(tokens)
