import numpy as np
import os
os.chdir(r'C:\Users\sfrie\Ydata\ydata_test_2\test2_attempt2')

input = open('d_input.txt').read().strip().split('\n')
input = [x.split(' ') for x in input]


 
rooks = [list(map(int, x)) for x in input]
n= rooks[0][0]
rooks.pop(0)
print(rooks)

N = n*n 
board = np.reshape(list(np.zeros(N)), [5,5])

for id in range(0, len(rooks)):  
    for row in range(1, n+1):  
        for column in range(1, n+1): ##When just leaving it as range(1, n), this gives a range of 1,2,3. However, we also need 4, in order to cover the last rows and columns. 
            if row == rooks[id][0] and column == rooks[id][1]:  ## Additonally, each conditional here needs -1 offsets in the change, to convert from the input (1, for example) to an index (0)
                board[row-1][column-1] = 1 ## the rook  
            if row == rooks[id][0] and column != rooks[id][1]:  
                board[row-1][column-1] = 2 ## attacked cell  
            if row != rooks[id][0] and column == rooks[id][1]:  
                board[row-1][column-1] = 2 ## attacked cell  
    print(board)
  
unattacked_cells = N ## number of unattacked cells  
for row in range(0, n):  
    for column in range(0, n):  
        if board[row][column] == 2 or board[row][column] ==1 :  
            unattacked_cells -= 1  
  
print(unattacked_cells)