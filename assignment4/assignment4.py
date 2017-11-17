from fst import *
from Tokenizer import *
import string

def part1():
	# 1. create file object with ex. file test.txt
	f = open('test.txt', 'r+') #read, a = make if not there

	# 2. create another file object to write to: siegle.txt
	siegle_text = open("siegle.txt", "w+") #write
	# 3. read file contents in as string and print length of string to output file
	# if f.mode == 'r+':
	contents =f.read()
	print "This file has", len(contents), "characters."
	#siegle_text.write("This file has %d\rcharacters.\n" % len(contents))
	char_line = "This file has " + str(len(contents))+ " characters.\n"
	siegle_text.write(char_line)
	# 4. read file in as list of lines and print how many lines are in file to output file
	# may need to add f.seek(0) here and in previous step to go back to beginning of file
	print "This file has", len(f.readlines()), "lines."
	
	# 5. print num words in each line to output file -> use split()
	f.seek(0)
	count = 0
	words = []
	line_line = "This file has " + str(len(f.readlines())) + " lines.\n"
	siegle_text.write(line_line)
	f.seek(0)
	for line in f:
		#words = len(line.split(' '))
		words.append(len(line.split()))
		line_to_write = "Line " + str(count) + " has " + str(words[count]) + " words."
		print line_to_write
		count +=1
		siegle_text.write(line_to_write)
		siegle_text.write("\n")
	siegle_text.close()

#part 2
#build set of strings, set of transitions -> pass to fst : using lab2
#read in file
def part2():
	minidict = open('minidictionary.txt', 'r')
	states = []
	lowercase = list(string.ascii_lowercase) #get lowercase alphabet source: https://stackoverflow.com/questions/16060899/alphabet-range-python
	fst_start  = "start"
	fst_final  = []
	fst_trans  = {"start" : {}}

	words = []
	arpabet_split  = []
	for line in minidict:
		spl = line.split() #split line
		words.append(spl[0]) #list of words
		arpabet_split.append(spl[1:]) #arpabet chars
	minidict.close()

	for i in range(0, len(words)):
	    if not words[i][0] in fst_trans:
	        states.append(words[i][0]) #new states to fst_states
	        fst_trans[words[i][0]] = {} #initial transitions from fst_start
	        fst_trans["start"][words[i][0]] = [words[i][:1], arpabet_split[i][0]+" "]

	for i in range(0, len(words)):
	    for j in range(1, len(words[i])):
	        states.append(words[i][:j+1]) #add new states to fst_states
	        fst_trans[words[i][:j+1]] = {}
	        fst_trans[words[i][:j]][words[i][j]] = [words[i][:j+1]]
	        if j < len(arpabet_split[i]): #silent letters at end of word
	            fst_trans[words[i][:j]][words[i][j]].append(arpabet_split[i][j]+" ")
	        else:
	            fst_trans[words[i][:j]][words[i][j]].append("")
	#build set of strings, transitions -> pass to fst
	ex = FST(lowercase, states, fst_start, words, fst_trans)

	print "test ", ex.transduce("red")
	for word in words:
		print "tranduced word: ", ex.transduce(word)

def part3():
	demo()

	    
def main():
	part1()
	part2()
	part3()

if __name__ == "__main__":
	main()
