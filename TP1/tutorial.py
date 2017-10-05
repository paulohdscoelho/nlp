In [1]: from gensim.models import word2vec

In [2]: import logging

In [3]: logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

In [4]: sentences = word2vec.Text8Corpus('text8')

In [5]: model = word2vec.Word2Vec(sentences, size=200)
2015-02-24 11:14:15,428 : INFO : collecting all words and their counts
2015-02-24 11:14:15,429 : INFO : PROGRESS: at sentence #0, processed 0 words and 0 word types
2015-02-24 11:14:22,863 : INFO : PROGRESS: at sentence #10000, processed 10000000 words and 189074 word types
2015-02-24 11:14:28,218 : INFO : collected 253854 word types from a corpus of 17005207 words and 17006 sentences
2015-02-24 11:14:28,362 : INFO : total 71290 word types after removing those with count&lt;5
2015-02-24 11:14:28,362 : INFO : constructing a huffman tree from 71290 words
2015-02-24 11:14:32,431 : INFO : built huffman tree with maximum node depth 22
2015-02-24 11:14:32,509 : INFO : resetting layer weights
2015-02-24 11:14:34,279 : INFO : training model with 1 workers on 71290 vocabulary and 200 features, using 'skipgram'=1 'hierarchical softmax'=1 'subsample'=0 and 'negative sampling'=0
2015-02-24 11:14:35,550 : INFO : PROGRESS: at 0.59% words, alpha 0.02500, 77772 words/s
2015-02-24 11:14:36,581 : INFO : PROGRESS: at 1.18% words, alpha 0.02485, 85486 words/s
2015-02-24 11:14:37,661 : INFO : PROGRESS: at 1.77% words, alpha 0.02471, 87258 words/s
...
2015-02-24 11:17:56,434 : INFO : PROGRESS: at 99.38% words, alpha 0.00030, 82190 words/s
2015-02-24 11:17:57,903 : INFO : PROGRESS: at 99.97% words, alpha 0.00016, 82081 words/s
2015-02-24 11:17:57,975 : INFO : training on 16718844 words took 203.7s, 82078 words/s

In [6]: model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)2015-02-24 11:18:38,021 : INFO : precomputing L2-norms of word weight vectors
Out[6]: [(u'wenceslaus', 0.5203313827514648)]

In [7]: model.most_similar(positive=['woman', 'king'], negative=['man'], topn=2) 
Out[7]: [(u'wenceslaus', 0.5203313827514648), (u'queen', 0.508660614490509)]

In [8]: model.most_similar(['man'])
Out[8]: 
[(u'woman', 0.5686948895454407),
 (u'girl', 0.4957364797592163),
 (u'young', 0.4457539916038513),
 (u'luckiest', 0.4420626759529114),
 (u'serpent', 0.42716869711875916),
 (u'girls', 0.42680859565734863),
 (u'smokes', 0.4265017509460449),
 (u'creature', 0.4227582812309265),
 (u'robot', 0.417464017868042),
 (u'mortal', 0.41728296875953674)]

In [9]: model.save('text8.model')
2015-02-24 11:19:26,059 : INFO : saving Word2Vec object under text8.model, separately None
2015-02-24 11:19:26,060 : INFO : not storing attribute syn0norm
2015-02-24 11:19:26,060 : INFO : storing numpy array 'syn0' to text8.model.syn0.npy
2015-02-24 11:19:26,742 : INFO : storing numpy array 'syn1' to text8.model.syn1.npy

In [10]: model.save_word2vec_format('text.model.bin', binary=True)
2015-02-24 11:19:52,341 : INFO : storing 71290x200 projection weights into text.model.bin

In [12]: model1 = word2vec.Word2Vec.load_word2vec_format('text.model.bin', binary=True)
2015-02-24 11:22:08,185 : INFO : loading projection weights from text.model.bin
2015-02-24 11:22:10,322 : INFO : loaded (71290, 200) matrix from text.model.bin
2015-02-24 11:22:10,322 : INFO : precomputing L2-norms of word weight vectors

In [13]: model1.most_similar(['girl', 'father'], ['boy'], topn=3)
Out[13]: 
[(u'mother', 0.6219865083694458),
 (u'grandmother', 0.556104838848114),
 (u'wife', 0.5440170764923096)]

In [14]: more_examples = ["he is she", "big bigger bad", "going went being"] 

In [15]: for example in more_examples:
   ....:     a, b, x = example.split()
   ....:     predicted = model.most_similar([x, b], [a])[0][0]
   ....:     print "'%s' is to '%s' as '%s' is to '%s'" % (a, b, x, predicted)
   ....:     
'he' is to 'is' as 'she' is to 'was'
'big' is to 'bigger' as 'bad' is to 'worse'
'going' is to 'went' as 'being' is to 'were'