import nltk
from nltk.corpus import mac_morpho


def simplify_tag(t):
     if "+" in t:
         return t[t.index("+")+1:]
     else:
         return t

tsents = mac_morpho.tagged_sents()
tsents = [[(w.lower(),simplify_tag(t)) for (w,t) in sent] for sent in tsents if sent]
train = tsents[100:]
test = tsents[:100]

tagger0 = nltk.DefaultTagger('n')
#print('Default tagger: ', accuracy(tagger0, test))
tagger1 = nltk.UnigramTagger(train, backoff=tagger0)
tagger2 = nltk.BigramTagger(train, backoff=tagger1)
print('Bigram: ',nltk.tag.api.evaluate(tagger2, test))
