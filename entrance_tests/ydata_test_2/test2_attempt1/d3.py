import numpy as np
file = open(r"C:\Users\sfrie\Ydata_practice\Test_2\d1.txt", "r")
n, m = [int(x) for x in file.readline().split(' ')]

rows_attacked = set()
cols_attacked = set()
for line in file:
    rows, cols = line.split()
    rows_attacked.add(rows)
    cols_attacked.add(cols)

not_attacked = (n -len(rows_attacked)) * (n-len(cols_attacked))
print(not_attacked)

