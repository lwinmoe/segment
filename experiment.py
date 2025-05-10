#!/usr/bin/python3
import os
import re
from subprocess import call, check_output

cnt = 0
MAX = 5
totalGold = 0
totalCorrect = 0
totalOut = 0

#inputF = 'mya-input.txt'
#goldF = 'mya-gold.txt'
inputF = 'test.input'
goldF = 'test.gold'

gold_lines = []

with open(goldF, 'r') as f:
    for line in f:
        if line != '\n':
            #print(line)
            gold_lines.append(line)


with open(inputF, 'r') as f:
    for line in f:
        if line == '\n':
            continue
        #if cnt > MAX:
        #    continue

        print("Sentence:", line)

        ####################### using segmenter ###################################
        output = check_output(["./segment" + " burmese.fst '" + line + "'"], shell=True)
        outStr = output.decode('utf-8')
        print(outStr)
        outStr = outStr.replace(" ", "|")
        outStr = outStr.replace("၊", "|၊|")
        outStr = outStr.replace("။", "|။")
        outStr = re.sub(r"(?P<punc>[\(\)\-\"\'])",r"|\g<punc>|", outStr)
        outStr = re.sub(r"(?P<eng>[0-9a-zA-Z]+)",r"|\g<eng>|", outStr)
        outStr = re.sub(r"(?P<bur_digits>[၀-၉,\.]+)",r"|\g<bur_digits>|", outStr)
        outStr = outStr.replace("||", "|")
        outStr = outStr.replace("\n", '')
        outItems = outStr.split("|")
        ####################### end using segmenter

        ####################### baseline #########################
        #line = line.replace("\n", "")
        #outItems = line.split(" ")
        ####################### end baseline #####################

        goldStr = gold_lines[cnt]
        goldStr = goldStr.replace("\n", '')
        goldItems = goldStr.split("  ")
        goldItems = [x for x in goldItems if x]
        print("GOLD:", goldItems)
        outItems = [x for x in outItems if x]
        correctItems = [x for x in outItems if x in goldItems]
        if outItems:
            totalGold += len(goldItems)
            totalCorrect += len(correctItems)
            totalOut += len(outItems)

            print("Gold cnt:", len(goldItems))
            print("Segmentation:", outItems)
            print("Segmented items cnt:", len(outItems))
            print("Correct items cnt:", len(correctItems))
            recall = len(correctItems) / len(goldItems) * 100
            print("Recall:", recall)
            precision = len(correctItems) / len(outItems) * 100
            print("Precision:", precision)
            print("===========================\n")
        cnt += 1

recall = round((totalCorrect / totalGold) * 100, 2)
precision = round((totalCorrect / totalOut) * 100, 2)
print("TotalOut:", totalOut)
print("totalGold:", totalGold)
print("totalCorrect:", totalCorrect)
print("Recall:", recall)
print("Precision:", precision)
