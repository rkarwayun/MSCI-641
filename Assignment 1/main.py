# https://www.w3schools.com/python/python_file_open.asp


import random
import re
import os
import sys


pos = list()
neg = list()
total = list()

total_valid = list()
total_with_stop = list()
total_no_stop = list()


# List from dorukcan's comment on this thread:
# https://gist.github.com/sebleier/554280
stop_list = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
             "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself",
             "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which",
             "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be",
             "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
             "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for",
             "with", "about", "against", "between", "into", "through", "during", "before", "after",
             "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
             "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all",
             "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not",
             "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don",
             "should", "now"]


# Function to read pos.txt
def readPos():
    f = open(positive, "r")
    for i in f:
        pos.append(i)
        total.append([i, 1])
    f.close()


# Function to read neg.txt
def readNeg():
    f = open(negative, "r")
    for i in f:
        neg.append(i)
        total.append([i, 0])
    f.close()


# Remove stop words from the tokenized list.
def remove_stop(s):
    ans = list()
    for i in s:
        if i.lower() in stop_list:
            pass
        else:
            ans.append(i)
    return ans


# Tokenize all the reviews.
def tokenize():

    # Regex cleaning and splitting by space, period, comma and single quotes.
    for i in total:
        sen = i[0]
        sen_no_punct = re.sub(r"!|\"|#|\$|%|&|\(|\)|\*|\+|/|:|;|<|=|>|@|\[|\\|\]|\^|`|\{|\|\}|~|\t|\n", ' ', sen)
        sen_split = re.split('[\.*]|[\,*]|[\'*]|[ *]', sen_no_punct)
        stop = list()
        for k in sen_split:
            if k != '':
                stop.append(k.lower())
        no_stop = remove_stop(stop)
        total_valid.append([sen, i[1]])
        total_with_stop.append([stop, i[1]])
        total_no_stop.append([no_stop, i[1]])


# Convert each tokenized review to a string for writing in output files.
def conv2str(words):
    ans = "["
    cnt = 0
    n = len(words)
    for i in words:
        ans = ans + "'" + i + "'"
        if cnt < n - 1:
            ans = ans + ", "
        cnt = cnt + 1
    ans = ans + "]"
    return ans


# Function to delete existing output files.
def delFiles():

    # Delete files (for debugging)
    os.remove("out.csv")
    os.remove("out_stop.csv")
    os.remove("train.csv")
    os.remove("train_stop.csv")
    os.remove("val.csv")
    os.remove("val_stop.csv")
    os.remove("test.csv")
    os.remove("test_stop.csv")
    os.remove("labels_all.csv")
    os.remove("labels_train.csv")
    os.remove("labels_val.csv")
    os.remove("labels_test.csv")


# Function to create output files.
def createFiles(n, n_train, n_val):

    # Creating the files.
    f1 = open("out.csv", "a")
    f2 = open("out_stop.csv", "a")
    f3 = open("train.csv", "a")
    f4 = open("train_stop.csv", "a")
    f5 = open("val.csv", "a")
    f6 = open("val_stop.csv", "a")
    f7 = open("test.csv", "a")
    f8 = open("test_stop.csv", "a")
    f9 = open("labels_all.csv", "a")
    f10 = open("labels_train.csv", "a")
    f11 = open("labels_val.csv", "a")
    f12 = open("labels_test.csv", "a")

    '''flag1 = True
    flag2 = True
    flag3 = True'''


    # Writing to files.
    for i in range(n):
        st = conv2str(total_no_stop[i][0])
        no_st = conv2str(total_with_stop[i][0])

        # print(st)
        f1.write(st + "\n")
        f2.write(no_st + "\n")
        f9.write(str(total_no_stop[i][1]) + "\n")
        if i < n_train:
            '''if flag1:
                print(st, str(total_no_stop[i][1])+"\n")
                flag1 = False'''

            f3.write(st + "\n")
            f4.write(no_st + "\n")
            f10.write(str(total_no_stop[i][1])+"\n")
        elif i < n_val:
            '''if flag2:
                print(st, str(total_no_stop[i][1])+"\n")
                flag2 = False'''
            f5.write(st + "\n")
            f6.write(no_st + "\n")
            f11.write(str(total_no_stop[i][1]) + "\n")
        else:
            '''if flag3:
                print(st, str(total_no_stop[i][1])+"\n")
                flag3 = False'''

            f7.write(st + "\n")
            f8.write(no_st + "\n")
            f12.write(str(total_no_stop[i][1]) + "\n")

    # Closing the files.
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    f9.close()
    f10.close()
    f11.close()
    f12.close()


# Main function.
def work():

    # Read the input files.
    readPos()
    readNeg()
    # print(len(neg), len(pos), len(total))

    # Shuffle the reviews.
    random.shuffle(total)

    # Tokenize.
    tokenize()

    n = len(total_with_stop)
    n_train = n * 0.8
    n_val = n_train + n * 0.1
    n_test = n_val + n * 0.1
    # print(n_train, n_val, n_test)

    # Create Output Files.
    createFiles(n, n_train, n_val)


if __name__ == '__main__':
    # print(sys.argv)
    if len(sys.argv) == 1:
        print("Reading files from default location.")
        positive = "pos.txt"
        negative = "neg.txt"
    elif len(sys.argv) == 2:
        print("Reading files from parent directory specified in the arguments.")
        positive = sys.argv[1] + "//pos.txt"
        negative = sys.argv[1] + "//neg.txt"
        # print(positive, negative)
    elif len(sys.argv) == 3:
        print("Reading files from location specified in the arguments.")
        positive = sys.argv[1]
        negative = sys.argv[2]
        # print(positive, negative)
    else:
        # print(sys.argv)
        print("Error in command line arguments, using files at present location.")
        positive = "pos.txt"
        negative = "neg.txt"

    # Uncomment to delete existing output files.
    # delFiles()

    # Executing the program.
    work()
