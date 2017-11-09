#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud
import sys

#d = path.dirname(__file__)

# Read the whole text.
text = open(sys.argv[1]).read().lower().strip()

text = text.replace('cataluna','cataluña').replace('referendum','referéndum')


# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig(str(sys.argv[1].split('/')[1].replace('.txt',''))+'.png')
#plt.show()

