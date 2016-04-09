#!/usr/bin/python3
import os
from subprocess import call, check_output

cnt = 0
MAX = 5
totalGold = 0
totalCorrect = 0
totalOut = 0

inputF = 'mya-input.txt'
goldF = 'mya-gold.txt'

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

        print(line)
        #output = os.system("./segment" + " burmese.fst '" + line + "'")
        #output = call("./segment" + " burmese.fst '" + line + "'", shell=True)
        output = check_output(["./segment" + " burmese.fst '" + line + "'"], shell=True)
        outStr = output.decode('utf-8')
        print(outStr)
        outStr = outStr.replace(" ", "|")
        outStr = outStr.replace("||", "|")

        outStr = outStr.replace("\n", '')

        outItems = outStr.split("|")
        goldStr = gold_lines[cnt]
        goldStr = goldStr.replace("\n", '')
        goldItems = goldStr.split("|")
        goldItems = [x for x in goldItems if x]
        print("GOLD:", goldItems)
        outItems = [x for x in outItems if x]

        correctItems = [x for x in outItems if x in goldItems]
        if outItems:
            totalGold += len(goldItems)
            totalCorrect += len(correctItems)
            totalOut += len(outItems)

            print(len(outItems))
            print(len(correctItems))
            recall = len(outItems) / len(goldItems) * 100
            print("Recall:", recall)
            precision = len(correctItems) / len(goldItems) * 100
            print("Precision:", precision)
            print(outItems)
            print("===========================\n")
        cnt += 1

recall = round((totalOut / totalGold) * 100, 2)
precision = round((totalCorrect / totalGold) * 100, 2)
print("TotalOut:", totalOut)
print("totalGold:", totalGold)
print("totalCorrect:", totalCorrect)
print("Recall:", recall)
print("Precision:", precision)