import string
letters = string.ascii_lowercase
string = "hello 1999 [5]. we are here-and that is great."
string = string.split()
sentence = []
for x in string:
    word = []
    for y in x:
        if y in letters:
            word.append(y)
    if word != []:
        add = ''.join(word)
        sentence.append(add)
print(sentence)
sentence = ' '.join(sentence)

print(sentence)

#string = string.replace('. ', '\n')