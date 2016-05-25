#!/usr/bin/python3

words = []
inputF = "chinese-word-list.txt"
outF = "chinese.scr"

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
    out.write('regex words @> "|" ... "|";\n')
    out.write('save stack chinese.fst\n')
    #out.write('print dot > burmese.dot\n')


