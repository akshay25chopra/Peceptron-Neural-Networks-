import os
import re
import json
import sys
from random import shuffle


spamY = 1
hamY = -1
uniqueWords = []
bias = 0


trainData = list()

def spam_regex(r):
    return re.search(r'(.)*spam(.)*', r)

def ham_regex(r):
    return re.search(r'(.)*ham(.)*', r)

def changeWeights(l, d, b):
    if l[-1] == "SPAM":
        for word in l[:-1]:
            d[word] += spamY
            b = b + spamY
    if l[-1] == "HAM":
        for word in l[:-1]:
            d[word] += hamY
            b = b + hamY



for root, dir, files in os.walk(sys.argv[1]):

    for name in files:
        if name not in ['.DS_Store', '_MACOSX']:
            with open(os.path.join(root, name), 'r', encoding="latin1") as f:
                file1 = f.read()
                file1 = file1.strip().split()

                if (spam_regex(root)):
                    trainData.append(file1 + ["SPAM"])
                    uniqueWords.extend(file1)

                elif (ham_regex(root)):
                    trainData.append(file1 + ["HAM"])
                    uniqueWords.extend(file1)

uniqueWords = set(uniqueWords)
initialDict = {value : 0.0 for value in uniqueWords}
#print(trainData)


for i in range (0,20):
    shuffle(trainData)

    for lists in trainData:
        alpha = 0
        for words in lists[:-1]:
            alpha = alpha + initialDict[words]

        alpha1 = alpha + bias

        if lists[-1] == "SPAM":
            y_alpha = alpha1 * spamY
        elif lists[-1] == "HAM":
            y_alpha =  alpha1 * hamY

        if y_alpha<=0:
            changeWeights(lists,initialDict,bias)


initialDict["secretcodenumber97020250694"] = bias


#print(initialDict)

with open('per_model.txt', 'w+', encoding='latin1') as a:
    json.dump(initialDict, a)

def main():
    if __name__ == "__main__":
        main()
