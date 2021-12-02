import numpy as np
def allcellspassed(maze, rows, cols):
    for r in range(1, rows+1):
        for c in range(1, cols+1):
            if maze[r][c] == "#":
                continue
            
            q = []
            visited = np.zeros((rows +2, cols +2)) #need double brackets to keep within first arg.
            visited[r,c] = 1
            q.append((r,c))

            while len(q) !=0:
                #make the next node in q the current node, by removing it from the q. 
                cur_r, cur_c = q.pop()
                #check all possible directions
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
                    next_r = cur_r +dr
                    next_c = cur_c + dc
                    #Validated the next move. Only move if the node is '.', and has already been visited.
                    if maze[next_r][next_c] == '.' and not visited[next_r, next_c]:
                        #Mark the node as "visited"
                        visited[next_r, next_c] = 1
                        #add the visited node to the q. This will then be checked once its turn in the q comes up, for neighbors.
                        q.append((next_r, next_c))
            #All possible paths have been checked and validated. Now, we must check if all of the '.'s have been passed through.

            true_count = np.sum(visited)
            period_count = sum(1 for x in maze for y in x if y == '.')
            if true_count == period_count:
                return "Yes"
            
    return "No"

 
    
file = open(r'C:\Users\sfrie\Ydata\ydata_test_1\test1_attempt1\d_input.txt').read().strip().split('\n')
rows, cols = map(int, file.pop(0).split())
#The following makes a border wall around our array. This will be used to check if th neighboring nodes of each node are valid.
maze = []
maze.append("#" * (cols + 2))
for row in file:
    maze.append("#" + row + "#") #readline will iterate to the next unread line of file.
maze.append("#" * (cols + 2))
print(allcellspassed(maze, rows, cols))