data = open('data.txt').read().strip().split('\n')
input = open('input.txt').read().strip()
input = int(input)
for line in range(len(data)):
    if line == input:
        print(len(set(data[line])))

        loc = max(data[line], key=data[line].count)
        print(loc)
