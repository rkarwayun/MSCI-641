# MSCI 641 Assignment 2

To run the file, use the following command:
```python main.py```

This assumes that you have the output files from the Assignment 1 in the same location as the python file.

If files are located at any other location, use the following command:
```python main.py path```
Where *path* is the parent folder where the files are located. In case *path* contains spaces, please enclose it in quotes.

Original Review Dataset is from https://github.com/fuzhenxin/textstyletransferdata/tree/master/sentiment.

**STOP-WORDS REMOVED**

Unigrams: 80.59%

Bigrams: 79.17%

Unigrams + Bigrams: 82.41%


**WITH STOP-WORDS**

Unigrams: 80.79%

Bigrams: 82.58%

Unigrams + Bigrams: 83.32%

2a) Model with stop-words performed better.
Stop-words can provide some important information about the sentence and context behind it. Removing them may change the meaning of the sentence. For example, “not”, “this” and “is” are stop-words in NLTK. Hence, both “This car is good” and “This car is not good” will be reduced to “car good” though they have completely opposite meanings. Hence, considering stop-words may help us with more information and hence is giving us slightly better results.

2b) Unigrams + Bigrams model performed the best.
For data without stop-words, unigrams performed better than bigrams. This can be attributed to the fact that bigrams can make the data matrix sparse which can lead to overfitting; also, removing stop words may result in pairings of remaining adjacent words (tokens) which may not be related and resulting text features would help little in classification and hence the performance in Bigrams is can be explained to not be at par with that of Unigrams.

For data with stop words, Bigrams performed better than Unigrams. This can be attributed to the fact that in case stop words are considered, the word pairings seemed to provide more context than just a single word, for example in some cases considering a couple of words may provide a new meaning (such as negation) and hence if stop words are considered, bigrams, as they have a chance of providing more context, are performing better than unigrams.

Unigrams + Bigrams model performed the best in both cases. Inclusion of Unigrams makes the data matrix less sparse than in the case of only Bigrams and Bigrams provide additional context than in case of just Unigrams which leads to better performance overall.
