sourcefile = open('article.txt')

stop_words = ['a','the','of','at','in','and','to']

new_lines = []

for line in sourcefile:
    words = line.split()
    new_line = []
    for word in words:
        if word not in stop_words:
            new_line.append(word)
    new_lines.append(new_line)

def count_ngram(ngram_dict,word_list,n):

    for num in range(0, len(word_list)-(n-1)):
        ngram = ' '.join(word_list[num:num+n])
        ngram_dict[ngram] = ngram_dict.get(ngram,0) + 1

    return ngram_dict

onegram_dict = dict()
twogram_dict = dict()
threegram_dict = dict()

for word_list in new_lines:
    onegram_dict = count_ngram(onegram_dict,word_list,1)
    twogram_dict = count_ngram(twogram_dict,word_list,2)
    threegram_dict = count_ngram(threegram_dict,word_list,3)

print(sorted([ (v,k) for k,v in onegram_dict.items() ], reverse=True)[0][1])
print(sorted([ (v,k) for k,v in twogram_dict.items() ], reverse=True)[0][1])
print(sorted([ (v,k) for k,v in threegram_dict.items() ], reverse=True)[0][1])