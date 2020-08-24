import numpy as np
import pandas as pd
import re
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
import warnings
import sys

ans = []

train = []
val = []
test = []
train_l = []
val_l = []
test_l = []
train_s = []
val_s = []
test_s = []


# Initialize lists.
def clear():
    global train, val, test, train_l, val_l, test_l, train_s, val_s, test_s
    train = []
    val = []
    test = []
    train_l = []
    val_l = []
    test_l = []
    train_s = []
    val_s = []
    test_s = []


# Function to read input files and append data to corresponding lists.
def load(filename, arr, isLabel):
    f = open(filename, "r")
    for i in f:
        st = re.sub(r"\[|\]|\,|\'|\n", '', i)
        if isLabel:
            arr.append(int(st))
        else:
            arr.append(st)
    f.close()


# Function to call the lead() function.
def loadInput():
    clear()
    load(parent + "train.csv", train, False)
    load(parent + "val.csv", val, False)
    load(parent + "test.csv", test, False)
    load(parent + "labels_train.csv", train_l, True)
    load(parent + "labels_val.csv", val_l, True)
    load(parent + "labels_test.csv", test_l, True)
    load(parent + "train_stop.csv", train_s, False)
    load(parent + "val_stop.csv", val_s, False)
    load(parent + "test_stop.csv", test_s, False)


# Function to vectorize the data.
def vector(kind, tr, va, te):
    if kind == 1:
        vectorizer = CountVectorizer(ngram_range=(1, 1))
    elif kind == 2:
        vectorizer = CountVectorizer(ngram_range=(2, 2))
    elif kind == 3:
        vectorizer = CountVectorizer(ngram_range=(1, 2))
    else:
        pass
    X_train = vectorizer.fit_transform(tr)
    X_val = vectorizer.transform(va)
    X_test = vectorizer.transform(te)
    return X_train, X_val, X_test


# This function trains the model with different hyper parameters and returns the hyper-parameter with best validation
# accuracy.
def trainModel(X_train, X_val):
    alpha = [0, 0.1, 0.2, 0.5, 1, 10, 20, 50, 100]
    maxi = 0
    hyper = 0
    for i in alpha:
        clf = MultinomialNB(alpha=i)
        clf.fit(X_train, train_l)
        y_pred = clf.predict(X_val)
        score = accuracy_score(val_l, y_pred)
        if score > maxi:
            maxi = score
            hyper = i
        # print(i, " = ", score)
    # print(maxi, hyper)
    return hyper


# Function to calculate test accuracy for the model.
def testModel(hyper, X_train, X_test, type1, type2):
    clf = MultinomialNB(alpha=hyper)
    clf.fit(X_train, train_l)
    y_pred = clf.predict(X_test)
    score = accuracy_score(test_l, y_pred)
    s = ""
    if not type1:
        s = s + "Without Stop Words; "
    else:
        s = s + "With Stop Words; "
    if type2 == 1:
        s = s + "Unigrams; Test Accuracy = "
    elif type2 == 2:
        s = s + "Bigrams; Test Accuracy = "
    elif type2 == 3:
        s = s + "Unigrams + Bigrams; Test Accuracy = "
    s = s + str(score * 100) + "%"
    ans.append(s)


# Function to run the cases where stop words are not considered.
def noStopModel():
    # print("\n\nWithout stop words:")
    for i in range(1, 4):
        # print(i)
        X_train, X_val, X_test = vector(i, train, val, test)
        hyper = trainModel(X_train, X_val)
        testModel(hyper, X_train, X_test, False, i)
    # Without stop words, unigram, best validation accuracy = 80.79% for alpha = 0.5
    # Without stop words, bigram, best validation accuracy = 79.52% for alpha = 1
    # Without stop words, unigram + bigram, best validation accuracy = 82.59% for alpha = 1


# Function to run the cases where stop words are considered.
def stopModel():
    # print("\n\nWith stop words:")
    for i in range(1, 4):
        # print(i)
        X_train, X_val, X_test = vector(i, train_s, val_s, test_s)
        hyper = trainModel(X_train, X_val)
        testModel(hyper, X_train, X_test, True, i)

    # With stop words, unigram, best validation accuracy = 80.77% for alpha = 0.5
    # With stop words, bigram, best validation accuracy = 82.83% for alpha = 0.5
    # With stop words, unigram + bigram, best validation accuracy = 83.43% for alpha = 0.5


# Main.
if __name__ == '__main__':

    warnings.filterwarnings("ignore")
    parent = ""
    if len(sys.argv) == 2:
        parent = sys.argv[1] + "/"

    # Load input into lists.
    loadInput()

    # ans stores our results.
    ans = []

    # Running for data without stop words.
    noStopModel()

    # Running for data with stop words.
    stopModel()

    # Printing the results.
    for i in ans:
        print(i)