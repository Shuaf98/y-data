
article = open(r'C:\Users\sfrie\Ydata\ydata_test_1\test1_attempt1\E1_Sample_Test1.txt')
stop_words = ['a', 'the', 'of', 'at', 'in', 'and', 'to']
working_file = []
for sentence in article:
    working_sentence = []
    sentence = sentence.split()
    for word in sentence:
        if word not in stop_words:
            working_sentence.append(word)
    working_file.append(working_sentence)

#Make a list of unique words
unique_words = []
for sentence in working_file:
    print(sentence)
    for y in sentence:
        if y not in unique_words:
            unique_words.append(y)

#Count number of sentences which contain the word
for word in unique_words:
    count = 0
    average_list = []
    for sentence in working_file :
        if word in sentence:
            count+=1
            length = len(sentence)
            average_list.append(len(sentence))
    average_length = sum(average_list)/ len(average_list)
    print(word, count, average_length)


