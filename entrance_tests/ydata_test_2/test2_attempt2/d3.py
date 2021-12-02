input = open('d_input.txt').read().strip().split('\n') ##Important to add in .strip(), in case of any leading or trailing space 
input = [x.split(' ') for x in input]
print(input)
rooks = [list(map(int, x)) for x in input]
print(rooks)

n= rooks[0][0]
rooks.pop(0)

rows = set()
cols = set()
for x in rooks:
    cols.add(x[0])
    rows.add(x[1])
missing_rows = (n- len(rows))
missing_cols = (n- len(cols))
sum = missing_rows * missing_cols
print(sum)