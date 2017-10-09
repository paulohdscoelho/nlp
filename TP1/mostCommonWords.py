from operator import itemgetter
import sys
import re
import collections
from stop_words import get_stop_words

book1 = sys.argv[1]
book2 = sys.argv[2]

stop_words = get_stop_words('english')

words_book1 = re.findall(r'\w+', open(book1).read())
dictWords1 = collections.Counter(words_book1)

topWords1 = {}

for word in dictWords1:
	if word.lower() not in stop_words:
		topWords1[word] = dictWords1[word]		

topWords1 = collections.Counter(topWords1).most_common(100)
print topWords1


words_book2 = re.findall(r'\w+', open(book2).read())
dictWords2 = collections.Counter(words_book2)

topWords2 = {}

for word in dictWords2:
	if word.lower() not in stop_words:
		topWords2[word] = dictWords2[word]		

topWords2 = collections.Counter(topWords2).most_common(100)
print topWords2

    