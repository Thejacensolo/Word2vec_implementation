#The Postagger Similarity Program (w2v_similarity_c.py)

@Author: Tibor Teske for Acoli

What is this Program:
w2v_similarity_c.py is an implementation of gensims word2vec, wich analyzes whole postagged files and replaces different word types with similar ones based on the Tags provided
by tools like the Stanford postagger. Additionally it shows the [replaced] word next to the replacing. Currently it is not context sensitive (f.e. good and bad are interchangable)
so use it with care. Also again a trained "myvecs.kv" file is needed. 

How to use:
Call "python w2v_similarity_c.py -pos [Tag] [Tag] ... -sim [Number]" without the cornered brackets. 

The Tagged file and input file have to be configurated under "txt_input_datei" (text file) and "meta_input_datei" (Postags). 
IMPORTANT: every single Entry in your input file has to match 1 to 1 wih your Postagged file.

"-pos" you can select wich kind of word you want to have replaced (f.e. NN = Noun, RB = Adverb etc.) full list here -> https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

"-sim" you can chose a number between 0 and 1 so the program only replaces words wich have a higher propability than the number given


an example of the required files is included (myvecs.kv, all-pos.txt, raw-sentence.txt)




#The Similarity Sentence Program (w2v_similarity_sentence.py)

@Author: Tibor Teske for Acoli

What is this Program:
w2v_sentence_similarity.py is an implementation of gensims word2vec, in wich you can insert a sentence and you are given back simmilar words for each word, with a grade (0-1)
on How good it fits. The Suggestions come from a word2vec trained model based on huge text files, and can be trained at will (with my "Trainer" software).
Ive included an exmpale "myvecs.kv" wich was trained on around 25GB of Papers/thesis in the Biochemical Field.

How to use:
just call "python w2v_similarity_sentence.py Your sentence here" (no parenthesis needed)
