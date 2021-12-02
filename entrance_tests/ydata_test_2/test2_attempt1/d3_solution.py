with open('input.txt') as f:
	n, m = [int(x) for x in f.readline().split(' ')]
	attacked_rows = set()
	attacked_columns = set()
	for line in f:
		row, column = line.split()
		# All we care is which row and which column
		attacked_rows.add(int(row))
		attacked_columns.add(int(column))

print((n-len(attacked_rows))*(n-len(attacked_columns)))