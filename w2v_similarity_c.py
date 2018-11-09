import gensim
import re
import csv
import logging
import sys
from gensim.models import KeyedVectors

### Main program
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Load word vectors
#loading input
vectors = KeyedVectors.load("myvecs.kv", mmap='r')
txt_input_datei = open("raw-sentences.txt","r")
meta_input_datei = open("all-pos.txt","r")
txt_input = txt_input_datei.read()
txt_input_datei.close()

meta_input = meta_input_datei.read()
meta_input_datei.close()
#Examples on how to use word vectors.
meta_input = meta_input.split("\n")
txt_input = txt_input.split("\n")
for i in range(len(txt_input[:-1])):
    txt_input[i] = txt_input[i].split(" ")

for i in range(len(meta_input[:-1])):
    meta_input[i] = meta_input[i].split(" ")



#generating all simmilar words v = list of a list of all alternatives
v = []
for x in range(len(txt_input)):
    v.append([])
    for j in range(len(txt_input[x])):
        if txt_input[x][j].lower() in vectors:
            v[-1].append(vectors.most_similar(txt_input[x][j].lower()))
        else:
            v[-1].append([["", 0.0]])


#input of Parameter
output_txt = ""
postagger = ""
#when not specified is the similarity threshold at 0.8
input_similarity = 0.8
parameter = sys.argv[1:]
pos = 0
sim = -1
for i in range(len(parameter)):
    if parameter[i] == "-pos":
        pos = i
     #   while True:
     #       postagger = parameter[i+1:]
     #       i = i + 1
     #       if parameter[i] == "-sim":
     #           i = i - 1
     #           break
    if parameter[i] == "-sim":
        sim = i
    #    input_similarity = parameter[i+1]

postagger = parameter[pos+1:sim]  
print(postagger)
float(input_similarity) 
        

#generating the output based on chosen specifications        
for s in range(len(txt_input)):
    for w in range(len(txt_input[s])):
        tupel = v[s][w]
        best_guess = tupel[0]
        similarity = best_guess[1]
        float(similarity)
        float(input_similarity)
        word = best_guess[0]
        pos = meta_input[s][w]
        if (pos in postagger) and (float(similarity) >= float(input_similarity)):
            output_txt += word + "[" + txt_input[s][w] + "] "
        else:
            output_txt += txt_input[s][w]
        output_txt += " "

print(output_txt)

