
import re
file = open(r'C:\Users\sfrie\Ydata\ydata_test_1\test1_attempt1\e1_article.txt')
file = file.read().lower().split('.')
print(file)

for line in file:
    new = ' '.join(re.findall("[a-z]+", line))
    print(new)