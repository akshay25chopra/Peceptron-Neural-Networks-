import re
import sys

def getStats():
    with open(sys.argv[1], 'r',encoding="latin1") as outputFile:
        data = outputFile.readlines()

    precision = {'spam':0.0, 'ham':0.0}
    recall = {'spam':0.0, 'ham':0.0}
    f1 = {'spam':0.0, 'ham':0.0}
    tp = [0.0,0.0]
    fp = [0.0,0.0]
    fn = [0.0,0.0]

    for key in data:
        key = key.strip('\n')
        key = key.split(' ')
        #print(key)
        if (key[0] != 'spam') and (re.search(r'(.)*spam(.)*', key[1])):
            fn[0] += 1
        elif (key[0] == 'spam') and (re.search(r'(.)*ham(.)*', key[1])):
            fp[0] += 1
        elif (key[0] != 'ham') and (re.search(r'(.)*spam(.)*', key[1])):
            tp[0] += 1

        if (key[0] != 'ham') and (re.search(r'(.)*ham(.)*', key[1])):
            fn[1] += 1
        elif (key[0] == 'ham') and (re.search(r'(.)*spam(.)*', key[1])):
            fp[1] += 1
        elif (key[0] != 'spam') and (re.search(r'(.)*ham(.)*', key[1])):
            tp[1] += 1


    precision['spam'] = round(tp[0] / (tp[0] + fp[0]), 2)
    recall['spam'] = round(tp[0] / (tp[0] + fn[0]), 2)
    f1['spam'] = round((2 * precision['spam'] * recall['spam']) / (precision['spam'] + recall['spam']), 2)

    precision['ham'] = round(tp[1] / (tp[1] + fp[1]), 2)
    recall['ham'] = round(tp[1] / (tp[1] + fn[1]), 2)
    f1['ham'] = round((2 * precision['ham'] * recall['ham']) / (precision['ham'] + recall['ham']), 2)

    with open("per_class2.txt", 'w+') as class2:
        class2.write("      Precision " + "Recall " + "F1" + '\n')
        class2.write("HAM   " + str(precision['ham']) + "       " + str(recall['ham']) + "    " + str(f1['ham']) + '\n')
        class2.write("SPAM  " + str(precision['spam']) + "      " + str(recall['spam']) + "    " + str(f1['spam']) + '\n')
        avg = (f1['spam'] + f1['ham']) / 2
        class2.write("Weighted Average: " + str(round(avg, 2)))

    class2.close()



getStats()