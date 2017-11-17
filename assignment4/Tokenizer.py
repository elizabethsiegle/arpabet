import string
# tokenizer takes a string and returns a list of the sentences contained in that string.
def tokenizer1(text):
   end_punctuation = ['.','!','?',':',';']
   sentence = ''
   sentences = []
   for c in text:
      if c in end_punctuation:
         sentence+=c
         sentences.append(sentence)
         sentence = ''
      else:
         sentence += c
   return sentences

def tokenizer2(text):
   end_punctuation  =  ['. ','! ','? ',': ','; '] #took out ; bc thought ; was complete sentence
   special_end_quote = ['." "']
   end_newline_punctuation = ['.\n','!\n','?\n',':\n',';\n']
   end_quotes_punctuation  =  ['."  ','!" ','?" ',':" ',';"']
   end_quotes_newline_punctuation = ['.\"\n','!\"\n','?\"\n',':\"\n',';\"\n']
   month_abbreviations    = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
   sentence = ''
   sentence_list = []
   index = 0
   while index < len(text):
      if text[index:index+3] in end_quotes_newline_punctuation: #quotation then new line
         sentence += text[index:index+2]
         sentence_list.append(sentence)
         sentence = ''
         index +=3
      elif text[index:index+4] in month_abbreviations: #month abbrev
         sentence += text[index:index+4]
         index += 4
      elif text[index] == '.' and text[index+1] == '"': #text[i:i+4] in special_end_quote: #doesn't work
         print "here"
         sentence += text[index:index+2]
         sentence_list.append(sentence)
         index += 2
      elif text[index] in list(string.ascii_uppercase) and text[index+1] == '.': #period after initial name
         sentence += text[index:index+2]
         index += 2
      elif text[index] == '\n': #new line
         index += 1
      elif text[index:index+4] in end_quotes_punctuation: #sentence end then quote then space
         sentence += text[index:index+4]
         sentence_list.append(sentence)
         sentence = ''
         i +=3
      elif text[index:index+2] in end_newline_punctuation: #sentence end+punctuation
         sentence += text[index]
         sentence_list.append(sentence)
         sentence = ''
         index += 3
      elif text[index:index+2] in end_punctuation: #sentence end w/ space
         sentence += text[index:index+2]
         sentence_list.append(sentence)
         sentence = ''
         index += 2
      else:
         sentence += text[index]
         index += 1
   return sentence_list

#takes list of strings and prints one at a time   
def print_sentences(sentence_list):
   i = 1
   for s in sentence_list:
      print 'Sentence',i,':',s
      i+=1
"""
Demonstration: rewrite demo() so that it 
1) opens the file tokenizertest.txt and reads it into a string
2) sends that string to tokenizer
3) sends the result of tokenizer to print_sentences
4) closes the file tokenizertest.txt
"""
def demo():
   input_file = open('tokenizertest.txt', 'r')
   input_string = input_file.read()
   string_tokens = tokenizer2(input_string)
   print_sentences(string_tokens)
   input_file.close()




