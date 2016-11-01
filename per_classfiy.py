import os
import re
import json
import sys



with open("per_model.txt", 'r',encoding="latin1") as fmodel:
    modelData = json.load(fmodel)


filename1 = sys.argv[2]
foutput = open(filename1, 'w+', encoding='latin1')

b = modelData['secretcodenumber97020250694']


for root, dirs, files in os.walk(sys.argv[1]):
    for name in files:
        tempDict = {}

        if name not in ['.DS_Store','_MACOSX']:
            with open(os.path.join(root,name), 'r',encoding="latin1") as f:
               # print(os.path.join(root,name))
                file1 = f.read()
                #file1 = file1.lower()
                file1 = file1.split()

                alpha1 = 0
                alpha = 0

                for k in range(0,len(file1)):
                    if file1[k] not in modelData:
                        alpha1 =alpha1 + 0
                    else:
                        alpha1 = alpha1 + modelData[file1[k]]

                alpha = alpha1 + b
                if (alpha>0):
                    foutput.write("spam ")
                else:
                    foutput.write("ham ")

                foutput.write(os.path.join(root,name)+"\n")
               # print(foutput)


foutput.close()

def main():
    if __name__ == "__main__":
        main()
