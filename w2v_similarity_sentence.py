import gensim
import re
import csv
import logging
import sys
from gensim.models import KeyedVectors
### Main program
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Load word vectors
vectors = KeyedVectors.load("myvecs.kv", mmap='r')
cmd_input = sys.argv[1:]
#Examples on how to use word vectors.
v = []
for j in cmd_input:
    if j.lower() in vectors:
        v.append(vectors.most_similar(j.lower()))

#print (v)
print ("Word    Similarity")
for k in v:
    tupel = k
    tupel_2 = tupel[0]
    similarity = tupel_2[1]
    word = tupel_2[0]
    print (word + "   " + str(similarity))



