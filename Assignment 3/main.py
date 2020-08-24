import sys
import re
import nltk
from gensim.models import Word2Vec
import os
import os.path
from os import path


# Reading the file (pos.txt and neg.txt) line by line and adding it to the list.
def readFile(name, rev):
    with open(name, "r") as f:
        for i in f:
            rev.append(re.sub(r"\n", '', str(i)).lower())
    return rev


# Reading the input files and returning thr dataframe.
def readInput():
    rev = list()
    rev = readFile(path1 + "pos.txt", rev)
    rev = readFile(path1 + "neg.txt", rev)
    print(len(rev))
    return rev


if __name__ == '__main__':

    # If no system argument is passed, it means that pos.txt and neg.txt are locally available.
    path1 = ""
    if len(sys.argv) == 2:
        path1 = sys.argv[1] + "/"

    # The Word2Vec model will be stored in the data/ folder. So if this folder does not exist, we explicitly create it.
    if not path.exists("data"):
        os.makedirs("data/")

    # Read the input.
    reviews = readInput()

    # https://stackoverflow.com/questions/37101114/what-to-download-in-order-to-make-nltk-tokenize-word-tokenize-work
    nltk.download('punkt')

    # Tokenize the reviews using nltk.
    # https://www.nltk.org/api/nltk.tokenize.html
    tokens = [nltk.word_tokenize(str(text)) for text in reviews]

    # Creating the Word2Vec model.
    # https://towardsdatascience.com/a-beginners-guide-to-word-embedding-with-gensim-word2vec-model-5970fa56cc92#e71b
    model = Word2Vec(tokens, min_count=20, size=250)

    # Saving the model.
    model.save('data/w2v.model')

    # Printing the 20 most similar words to 'good' and 'bad'.
    print("Words similar to 'good' are: ", model.wv.most_similar('good', topn=20), "\n\n")
    print("Words similar to 'bad' are: ", model.wv.most_similar('bad', topn=20), "\n\n")
