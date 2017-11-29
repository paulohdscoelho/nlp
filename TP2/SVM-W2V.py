
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import time
from gensim.models import Word2Vec as wv
from gensim.models.word2vec import LineSentence
from scipy import sparse
from collections import defaultdict
from sklearn import svm


# In[2]:


def leitura_arquivo(path):
    f1 = open(path, 'r')
    text = []
    tags = []
    word_tags = defaultdict(list)
    #leio arquivo e crio uma lista [word,tag]
    for line in f1:
        tokens = line.split()
        for token in tokens:
            word =  token.split('_')[0]
            tag =  token.split('_')[1]
            text.append(word)
            tags.append(tag)
            if tag not in word_tags[word]:
                word_tags[word].append(tag)

    return text,tags, word_tags

def words_to_num(text):
    words = {text[0][0]: 0, text[1][0]: 0}
    tags = {text[0][1]: 0, text[1][1]: 0}
    
    for i in range(2,len(text)):
        words[text[i][0]] = 0
        tags[text[i][1]] = 0
    
    #agora tenho um número único para cada palavra/tag
    return np.array(list(words.keys()) + list(tags.keys()))

def cria_dict_num(num_of_words):
    num_dict = {}
    for i in range(len(num_of_words)):
        num_dict[num_of_words[i]] = i
    return num_dict


# In[3]:


get_ipython().run_cell_magic('time', '', "path = 'macmorpho-train.txt'\ntext,tags, word_tags = leitura_arquivo(path)\ntext = np.array(text)")

# In[4]:


get_ipython().run_cell_magic('time', '', 'model = wv(text.reshape(-1,1), size = 400, min_count=1, window=10, iter=10)')


# In[5]:


X_train = []
for palavra in model.wv.vocab:
    X_train.append(model.wv[palavra])


# In[6]:


tag_dict = {}
word_dict = {}
i = 0
j = 0
for tag in tags:
    tag_dict[tag] = 0
for tag in tag_dict.keys():
    tag_dict[tag] = i
    i += 1
for word in model.wv.vocab:
    word_dict[word] = j
    j += 1
vec_tag = np.array(list(tag_dict.keys()))
vec_word = np.array(list(model.wv.vocab))


# In[7]:


mtx = sparse.lil_matrix((len(vec_word), len(vec_tag)))


# In[8]:


get_ipython().run_cell_magic('time', '', 'for i in range(len(text)):\n    mtx[word_dict[text[i]],tag_dict[tags[i]]] = 1')


# In[9]:

with open('SVM.dat','w') as saida:
    saida.write('Tag\tRBF score\n')
    for key, value in tag_dict.items():
        indx = value
        etiqueta = key
        print('Training for tag ',etiqueta)
        Y_train = []
        
        for i in range(len(vec_word)):
            Y_train.append(mtx[i,indx])
        print Y_train
        # In[10]:
        '''%%time
        clf = svm.SVC()
        clf.fit(X_train,Y_train)'''

        # In[11]:

        '''teste = clf.score(X_train[:150], Y_train[:150])
        teste'''

        # In[10]:

        get_ipython().run_cell_magic('time', '', 'X = X_train[:20000]\ny = Y_train[:20000]')

        # In[11]:

        get_ipython().run_cell_magic('time', '', "svr_rbf = svm.SVC(kernel='rbf', C=1e3, gamma=0.1)\n#svr_lin = svm.SVC(kernel='linear', C=1e3)\n#svr_poly = svm.SVC(kernel='poly', C=1e3, degree=2)\ny_rbf = svr_rbf.fit(X, y)#.predict(X)\n#y_lin = svr_lin.fit(X, y)#.predict(X)\n#y_poly = svr_poly.fit(X, y)#.predict(X)")

        # In[14]:

        get_ipython().run_cell_magic('time', '', 'clf = svm.SVC()\nclf.fit(X,y)')

        # In[ ]:

        '''print(y_lin.score(X,y),
        y_poly.score(X,y),
        y_rbf.score(X,y))'''

        # In[ ]:

        #print(y_poly.score(X,y))

        # In[ ]:

        #print(y_lin.score(X,y))

        # In[16]:
        
        saida.write(etiqueta+'\t'+str(y_rbf.score(X,y))+'\n')

        # In[12]:

        print('Rbf Score: ',y_rbf.score(X,y))
