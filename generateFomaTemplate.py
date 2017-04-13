#!/usr/bin/python3
'''
Read in a word list (each line is a word) and converts it to .scr which is the file foma wants
Lwin Moe, Hai Hu
'''
import sys, re

def convert(inputF, outF):
	words = []
	fileroot = inputF.replace('.txt','')

	##########################################
	# add "" between reserved symbols for foma:
	
	# All symbols in the ASCII range except [1-9A-Za-z'=] are reserved and need to be escaped
	# https://github.com/jrwdunham/foma/blob/master/foma/README.symbols
	# ASCII 0-9: 48-57 (inclusive), A-Z: 65-90, a-z: 97-122, ': 39, ?: 63, ": 34
	#  u\001A
	# full-width space \u3000

	regex = [0]*6
	regex[0] = re.compile("([\u0000-\u0021])")
	regex[1] = re.compile("([\u0023-\u002F])") # quotation mark " is excluded here, which is \u0022
	regex[2] = re.compile("([\u003A-\u0040])")
	regex[3] = re.compile("([\u005B-\u0060])")
	regex[4] = re.compile("([\u007B-\u00FF])")

	regex[5] = re.compile("([\u03A3\u03B5\u2192\u2194"
		"\u2200\u2203\u2205\u2208\u2218\u2225\u2227\u2228\u2229\u222A"
		"\u2264\u2265\u227A\u227B])") 
	##########################################

	unwanted = re.compile("([\u0000-\u001F])")

	with open(inputF, 'r') as f:
	    for line in f:
	        if line != '\n':
	            line = line.rstrip('\n') # only strip off \n, not \s
	            if len(line) > 1:
	            	print('line **{}** length > 1'.format(line))

	            # skip space/tab
	            if line == "\u0020" or line == "\t" or line == "\u3000":
	            	print('space/tab skipped!')
	            	continue

	            m = unwanted.match(line)
	            if m:
	            	print("unwanted line: {}".format(line))
	            	continue

	            if "0" in line:
	            	print("0 skipped!")
	            	continue

	            if "?" in line:
	            	print("? skipped!")
	            	continue

	            # print unicode code point
	            # print('unicode for {} is {}'.format(str(line), str(' '.join([str(ord(str(x))) for x in line]))))

				# for quotation marks, add %, and then continue
	            if "\"" in line:
	            	line = line.replace("\"", "%\"")
	            	words.append(line)
	            	continue
	            
	            # for other reserved symbols
	            for reg in regex:
	            	line = reg.sub('\"\g<1>\"', line) # add "" around symbols like ! @ ...
	            words.append(line)
	        else:
	        	print('empty line skipped!')
	
	print('first ten words:', words[:10])
	print('len[words]:', len(words))
	wordsStr = "|".join(words)
	#print (wordsStr)

	#define words [these|are|burmese|words|separated|by|pipe];
	#regex words @> "|" ... ;

	with open(outF, 'w') as out:
	    out.write("define words [" + wordsStr + "];\n")
	    out.write('regex words @> " " ... " " ;\n')
	    out.write('save stack ' + fileroot + '.fst\n')
	    #out.write('print dot > burmese.dot\n')

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Usage: python3 generateFomaTemplate.py fn_wordlist(.txt) fn_out(.scr)')
		exit(1)
	else:
		convert(sys.argv[1], sys.argv[2])
