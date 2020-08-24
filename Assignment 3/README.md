# MSCI 641 Assignment 3

**1) First run main.py with the following command:**

```python main.py``` : If pos.txt and neg.txt are available locally or

```python main.py path``` : Where *path* is the path to the folder that contains the above txt files. If the *path* contains space, please enclose it in quotes.

This would create the Word2Vec model and store it in *data/* folder.

**2) Run inference.py file:**
```python inference.py fileWithPath``` : *fileWithPath* contains the path of the txt file along with name which contains the list of words that are to be used for finding top-20 similar words. This assumes that the Word2Vec model exists and is present in *data/* as *w2v.model*. If the *fileWithP	ath* contains space, please enclose it in quotes.




# Report

Most of the words found similar to 'good' are positive in nature and similar to 'bad' are negative, however, there are some exceptions. Like  'bad', 'poor' and 'terrible' were found to be similar to 'good'; and 'good' and 'funny' were found similar to 'bad'. This can happen if contrasting words appear close to each other often in the data which can occur in these cases:

1) In case people use double negatives, like "This product is no good, it is quite bad.", which would lead to words with contrasting meanings appear near to each other.
2) If the reviewer is speaking about different things in the same review, he/she may say one is 'good' and the other is 'bad', again resulting in words with contrasting meanings appear near to each other.
3) The reviewer may use sarcasm which may result in words with contrasting meanings appear near to each other.

```
Top 20 words most similar to ' good ' are:
great : 0.744400680065155
decent : 0.733798623085022
terrific : 0.6711602210998535
fantastic : 0.6642747521400452
nice : 0.6553243398666382
superb : 0.6368108987808228
wonderful : 0.6133161783218384
fabulous : 0.6131844520568848
bad : 0.6010439395904541
impressive : 0.5923100709915161
excellent : 0.5900230407714844
poor : 0.5742269158363342
reasonable : 0.5602880716323853
terrible : 0.5477452874183655
pleasant : 0.5410994291305542
neat : 0.5360026359558105
amazing : 0.5345301032066345
awesome : 0.5332072377204895
promising : 0.5292213559150696
ok : 0.5261529088020325


Top 20 words most similar to ' bad ' are:
horrible : 0.6034621000289917
good : 0.6010439395904541
terrible : 0.5921584963798523
funny : 0.5483899116516113
poor : 0.5463659763336182
awful : 0.5328032970428467
lame : 0.5293092727661133
weird : 0.5283388495445251
fake : 0.5100970268249512
scary : 0.5061016082763672
strange : 0.5021688938140869
gross : 0.4987564980983734
obvious : 0.49783432483673096
stupid : 0.49210771918296814
shabby : 0.4908263385295868
nasty : 0.4892534017562866
weak : 0.4807630479335785
sad : 0.4737847149372101
salty : 0.4679880738258362
harsh : 0.4625985026359558

```