import sys
from gensim.models import Word2Vec
import re


# Reading the input txt file.
def readInput():
    inp = list()
    with open(path, "r") as f:
        for i in f:
            inp.append(re.sub(r"\n", '', str(i)).lower())
    return inp


# Finding top 20 most similar words from the dataset.
def printSimilar():
    for i in words:
        try:
            print("Top 20 words most similar to '", i, "' are:",)
            similar = model.wv.most_similar(i, topn=20)
            for j in similar:
                print(j[0], ":", j[1])
        except:
            print("Word '", i, "' is not in the vocabulary.")
        finally:
            print("\n\n")


if __name__ == '__main__':
    # The path (including the name of the txt file) needs to be specified.
    if len(sys.argv) < 2:
        print("Please specify the path to the text file.")
        exit(-1)
    path = sys.argv[1]

    # Reading the input words whose similar words need to be found.
    words = readInput()

    # Loading the Word2Vec model.
    model = Word2Vec.load('data/w2v.model')

    # Finding the similar words.
    printSimilar()
