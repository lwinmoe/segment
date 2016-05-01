#!/usr/bin/python3

words = []
inputF = "burmese-word-list.txt"
outF = "burmese.scr"

with open(inputF, 'r') as f:
    for line in f:
        if line != '\n':
            #print(line)
            line = line.rstrip()
            words.append(line)
#print (words)
wordsStr = "|".join(words)
#print (wordsStr)

#define words [these|are|burmese|words|separated|by|pipe];
#regex words @> "|" ... ;

with open(outF, 'w') as out:
    out.write("define words [" + wordsStr + "];\n")
    out.write('regex words @> "|" ... ;\n')
    out.write('save stack burmese.fst\n')
    out.write('print dot > burmese.dot\n')


