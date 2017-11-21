
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd
import time
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from scipy import sparse


# In[19]:


def leitura_arquivo(path):
    f1 = open(path, 'r')
    text = [[' ',' '],[' ',' '],[' ',' ']]
    tags = []
    #leio arquivo e crio uma lista [word,tag]
    for line in f1:
        tokens = line.split()
        for token in tokens:
            text.append( token.split('_'))
            #tags.append( token.split('_')[1])

    text.append([' ',' '])
    text.append([' ',' '])
    text.append([' ',' '])
    return text

def words_to_num(text):
    words = {text[0][0]: 0, text[1][0]: 0, text[2][0]: 0}
    tags = {text[0][1]: 0, text[1][1]: 0, text[2][1]: 0}
    
    for i in range(3,len(text)):
        try:
            words[text[i][0]] = 0
        except:
            print (i, text[i][0])
        tags[text[i][1]] = 0
    
    #agora tenho um número único para cada palavra/tag
    return np.array(list(words.keys()) + list(tags.keys()))

def cria_dict_num(num_of_words):
    num_dict = {}
    for i in range(len(num_of_words)):
        num_dict[num_of_words[i]] = i
    return num_dict


# In[20]:


def cria_ngram(text):
    ngram = []
    for i in range(3,len(text)-3):
        ngram.append([text[i-3][0],text[i-3][1], text[i-2][0],text[i-2][1], text[i-1][0],text[i-1][1], text[i][0], text[i+1][0], text[i+2][0], text[i+3][0]])
    return ngram


# In[21]:


path = 'macmorpho-train.txt'
text = leitura_arquivo(path)
word_number = words_to_num(text)
dict_num = cria_dict_num(word_number)
flags = np.array(list(dict_num[text[i][1]] for i in range(3,len(text)-3)))
#ngram = ['prev_prev_prev_word','prev_prev_prev_tag','prev_prev_word','prev_prev_tag','prev_word','prev_tag', 'curr_word', 'next_word','next_next_word','next_next_next_word']
ngram = cria_ngram(text)


# In[22]:


mtx = sparse.lil_matrix((len(ngram),len(word_number)+2), dtype=np.int8)


# In[ ]:


mtx.shape


# In[ ]:


get_ipython().run_cell_magic('time', '', 'for i in range(len(ngram)-2):\n    for word in ngram[i]:\n        mtx[i,dict_num[word]]+=1\n    mtx[i,len(word_number)-2] = len(ngram[i][6])\n    if ngram[i][6].islower():\n        mtx[i,len(word_number)-1] = 1\n    else:\n        mtx[i,len(word_number)-1] = 0\n                ')


# In[ ]:


get_ipython().run_cell_magic('time', '', 'train_x = mtx\ntrain_y = flags\n\nmodel = MultinomialNB()\nclf = model.fit(train_x,train_y)')


# In[ ]:


teste = clf.score(mtx,flags)
teste


# In[10]:


#teste 


# In[11]:


path = 'macmorpho-test.txt'
text = leitura_arquivo(path)


# In[12]:


#gero fgram do tipo ['prev_prev_word','prev_word', 'curr_word', 'next_word']
ngram_teste = []
for i in range(3,len(text)-3):
    ngram_teste.append([text[i-3][0],text[i-3][1], text[i-2][0],text[i-2][1], text[i-1][0],text[i-1][1], text[i][0], text[i+1][0], text[i+2][0], text[i+3][0]])   


# In[13]:


mtx = sparse.lil_matrix((len(ngram_teste),len(word_number)+2), dtype=np.int8)


# In[14]:


get_ipython().run_cell_magic('time', '', "for i in range(len(ngram_teste)):\n    for word in ngram_teste[i]:\n        try:\n            mtx[i,dict_num[word]]+=1\n        except:\n            mtx[i,dict_num[' ']]+=1\n    mtx[i,len(word_number)-2] = len(ngram_teste[i][6])\n    if ngram_teste[i][6].islower():\n        mtx[i,len(word_number)-1] = 1\n    else:\n        mtx[i,len(word_number)-1] = 0")


# In[15]:


flags_teste = np.array(list(dict_num[text[i][1]] for i in range(3,len(text)-3)))


# In[16]:


print(mtx.shape,
len(flags_teste))


# In[17]:


clf.score(mtx,flags_teste)

