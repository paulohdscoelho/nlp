#You have to download the spanish stopwords first with nltk.download()
import nltk  
from nltk.corpus import stopwords  
from nltk import word_tokenize  
from nltk.data import load  
from nltk.stem import SnowballStemmer  
from string import punctuation  
from sklearn.feature_extraction.text import CountVectorizer       
from sklearn.svm import LinearSVC  
from nltk.corpus import cess_esp as corpusSpanish
import sys
'''
#stopword list to use
spanish_stopwords = stopwords.words('spanish')

#spanish stemmer
stemmer = SnowballStemmer('spanish')

#punctuation to remove
non_words = list(punctuation)  
#we add spanish punctuation
non_words.extend(['¿', '¡'])  
non_words.extend(map(str,range(10)))

stemmer = SnowballStemmer('spanish')  
def stem_tokens(tokens, stemmer):  
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):  
    # remove punctuation
    text = ''.join([c for c in text if c not in non_words])
    # tokenize
    tokens =  word_tokenize(text)

    # stem
    try:
        stems = stem_tokens(tokens, stemmer)
    except Exception as e:
        print(e)
        print(text)
        stems = ['']
    return stems

vectorizer = CountVectorizer(  
                analyzer = 'word',
                tokenizer = tokenize,
                lowercase = True,
                stop_words = spanish_stopwords)

pipeline = Pipeline([  
    ('vect', vectorizer),
    ('cls', LinearSVC()),
])

#we build a Pipeline object
pipeline = Pipeline([  
    ('vect', CountVectorizer(
            analyzer = 'word',
            tokenizer = tokenize,
            lowercase = True,
            stop_words = spanish_stopwords,
            min_df = 50,
            max_df = 1.9,
            ngram_range=(1, 1),
            max_features=1000
            )),
    ('cls', LinearSVC(C=.2, loss='squared_hinge',max_iter=1000,multi_class='ovr',
             random_state=None,
             penalty='l2',
             tol=0.0001
             )),
])

#we fit the pipeline with the TASS corpus
pipeline.fit(tweets_corpus.content, tweets_corpus.polarity_bin)  
#now we predict on the new tweets dataset
tweets['polarity'] = pipeline.predict(tweets.tweet)  



# here we define the parameter space to iterate through
parameters = {  
    'vect__max_df': (0.5, 1.9),
    'vect__min_df': (10, 20,50),
    'vect__max_features': (500, 1000),
    'vect__ngram_range': ((1, 1), (1, 2)),  # unigrams or bigrams
    'cls__C': (0.2, 0.5, 0.7),
    'cls__loss': ('hinge', 'squared_hinge'),
    'cls__max_iter': (500, 1000)
}


grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1 , scoring='roc_auc')  
grid_search.fit(tweets_corpus.content, tweets_corpus.polarity_bin)  

'''
espWords = nltk.corpus.cess_esp.words()
espParsedSents = nltk.corpus.cess_esp.sents()
print(espParsedSents[0])
