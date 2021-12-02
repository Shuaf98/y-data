import numpy as np
#Function to check if all '.'s have been traversed
def allcellspassed(maze, rows, cols):
    #This loop starts changes the starting node.
    for r in range(1, rows+1):
        for c in range(1, cols+1):
            if maze[r][c] == "#":
                continue
            #We make a Queue to keep track of the current node, as well as all neighboring nodes.
            #We will also make a boolean numpy array, to track each node and if it equals True or False (visited or not)
            q = []
            visited = np.zeros((rows +2, cols +2)) #need double brackets to keep within first arg.
            q.append((r,c))

            while len(q) !=0: #While there are more neighboring nodes..
                #make the next node in q the current node, by removing it from the q. 
                cur_r, cur_c = q.pop()
                #check all possible directions
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
                    next_r = cur_r +dr
                    next_c = cur_c + dc
                    #Validate the next move, only move if the node is '.', and has already been visited.
                    if maze[next_r][next_c] == '.' and not visited[next_r, next_c]:
                        #Mark the node as "visited"
                        visited[next_r, next_c] = 1
                        #add the visited node to the q. This will then be checked for it's neighbords once it's turn in the q comes up.
                        q.append((next_r, next_c))
            #All possible paths have been checked and validated. Now, we must check if all of the '.'s have been passed through.


###This is the optimized section. The code would unnecessarily keep switching all_passed from true to false on every iteration.
###Here, we don't have to keep saving a variable.
            for check_r in range(1, rows + 1):
                for check_c in range(1, cols + 1):
                    if maze[check_r][check_c] == '.' and visited[check_r, check_c] == 0:
                        print("No")
                        return
            print("Yes")
            return
    ##Alternate method to check for untraversed '.'s
    #         true_count = np.sum(visited) #This numpy function counts trues in the array.
    #         period_count = sum(1 for x in maze for y in x if y == '.')
    #         if true_count == period_count:
    #             return True      
    # return False            
                     
file = open(r"C:\Users\sfrie\Ydata_practice\Test_1\inputD_2.txt", 'r')
line = file.readline()
rows, cols = map(int, line.split()) # split first line into two integers, to pass into the funciton we will make.
#The following makes a border wall around our array.
maze = []
maze.append("#" * (cols + 2))
for row in range(rows):
    maze.append("#" + file.readline() + "#")
maze.append("#" * (cols + 2))

allcellspassed(maze, rows, cols)
