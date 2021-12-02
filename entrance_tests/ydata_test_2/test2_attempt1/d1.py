import numpy as np
file = open(r"C:\Users\sfrie\Ydata_practice\Test_2\d1.txt", "r").readlines()
rooks = [list(x.split()) for x in file]
n = int(rooks[0][0])
m = int(rooks[0][1])
N = n*n

# input:  
# N - size of the chess board  
# rooks - 2D array of integers, rooks[i][0] is a row and rooks[i][1] is a column  


board = np.zeros(N).reshape(n,n)
rooks.pop(0)
for id in range(len(rooks)):
    for row in range(1, n+1):  
        for column in range(1, n+1): 
            if row == int(rooks[id][0]) and column == int(rooks[id][1]):  
                board[row-1][column-1] = 1 # the rook  
            if row == int(rooks[id][0]) and column != int(rooks[id][1]):  
                board[row-1][column-1] = 2 # attacked cell  
            if row != int(rooks[id][0]) and column == int(rooks[id][1]):  
                board[row-1][column-1] = 2 # attacked cell  
  

# unattacked_cells = N  # number of unattacked cells  
# for row in range(1, n+1):  
#     for column in range(1, n+1):  
#         if board[row-1][column-1] == 2 or board[row-1][column-1] == 1:  
#             unattacked_cells -= 1  
array = np.array(board)
print(N - np.count_nonzero(board))
