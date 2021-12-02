#Upload article file, and delete the stop words.
article = open(r'C:\Users\sfrie\Ydata\ydata_test_1\test1_attempt1\E1_Sample_Test1.txt')
old_text = article

stop_words = ['a', 'the', 'of', 'at', 'in', 'and', 'to']
old_text = old_text.read().split()
new_text = []
for x in old_text:
    if x not in stop_words:
        new_text.append(x)

#Count the most frequent word
max_word = max(new_text, key=new_text.count)
print(max_word)

#Create a dictionary to keep track of every gram, with its counts
gram_2 = {}
gram_3 = {}
#create three variables, as the current three words
word_1 = 0
word_2 = 1
word_3 = 2
length = len(new_text)

for x in new_text:
    while word_3 < len(new_text):
        two_gram = new_text[word_1] + ' ' + new_text[word_2]
        #two_gram = ' '.join([new_text[word_1], new_text[word_2]])
        if two_gram not in gram_2:
            gram_2[two_gram] = 1
        else:
            gram_2[two_gram] +=1
#Most frequent 3gram
        three_gram = new_text[word_1] + ' ' + new_text[word_2] + ' ' + new_text[word_3]
        #three_gram = ' '.join([new_text[word_1], new_text[word_2], new_text[word_3]])
        if three_gram not in gram_3:
            gram_3[three_gram] = 1
        else:
            gram_3[three_gram] += 1

        word_1 +=1
        word_2 +=1
        word_3 +=1
        
print(max(gram_2, key = gram_2.get))
print(max(gram_3, key = gram_3.get))
