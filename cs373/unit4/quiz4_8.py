# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------

    # Make another grid to keep track of our movements
    closed_nodes = [[0]*len(grid[0]) for i in range(len(grid))]
    open_nodes = [[0,init[0],init[1]]]
    closed_nodes[init[0]][init[1]] = 1
    while len(open_nodes) > 0:
        gval, row, col = open_nodes.pop(0)

        if [row,col] == goal:
            return [gval,row,col]
        else:
            for drow,dcol in delta:
                trow,tcol = row + drow , col + dcol
                if trow >= 0 and trow < len(grid) and tcol >= 0 and tcol < len(grid[0]):
                    if grid[trow][tcol] == 0 and not closed_nodes[trow][tcol]:
                        closed_nodes[trow][tcol] = 1
                        open_nodes.append([gval+cost,trow,tcol])


    return 'fail'


print search()
