import os
import re
import json
import sys
from random import shuffle


spamY = 1
hamY = -1
uniqueWords = []
bias = 0
avg_bias = 0
count = 1


trainData = list()

def spam_regex(r):
    return re.search(r'(.)*spam(.)*', r)

def ham_regex(r):
    return re.search(r'(.)*ham(.)*', r)

def changeWeights(l,iD,fD,b0,ab0,c):
    if l[-1] == "SPAM":
        for word in l[:-1]:
            iD[word] += spamY
            fD[word] += spamY * c
            ab0 = ab0 + (spamY * c)
            b0 = b0 + spamY

    if l[-1] == "HAM":
        for word in l[:-1]:
            iD[word] += hamY
            fD[word] += hamY * c
            ab0 = ab0 + (hamY * c)
            b0 = b0 + hamY

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
finalDict = {val : 0.0 for val in uniqueWords}

#print(trainData)


for i in range (0,30):
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
            changeWeights(lists,initialDict,finalDict,bias,avg_bias,count)


        count = count +1

for w in finalDict:
    finalDict[w] = round(initialDict[w] - ((1/count)*finalDict[w]),2)

avg_bias = round(bias - ((1/count)*avg_bias),2)

finalDict["secretcodenumber97020250694"] = avg_bias


#print(finalDict)

with open('per_model.txt', 'w+', encoding='latin1') as a:
    json.dump(finalDict, a)

def main():
    if __name__ == "__main__":
        main()
