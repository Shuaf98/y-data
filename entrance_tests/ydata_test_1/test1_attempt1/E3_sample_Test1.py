sourcefile = open(r"C:\Users\sfrie\Ydata_practice\E1_Sample_Test1.txt", "r")

stop_words = ['a','the','of','at','in','and','to']

new_lines = []
word_dict = {}
sentence_count = {}
sentence_total_length = {}

for line in sourcefile:
    words = line.split()
    new_line = []
    for word in words:
        if word not in stop_words:
            new_line.append(word)
            word_dict[word] = word_dict.get(word,1)
    new_lines.append(new_line)

for line in new_lines:
    for word in word_dict.keys():
        if word in line:
            sentence_count[word] = sentence_count.get(word,0) + 1
            sentence_total_length[word] = sentence_total_length.get(word,0) + len(line)

for word in word_dict.keys():
    print(word, sentence_count[word], sentence_total_length[word]/sentence_count[word])