# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D() below.
#
# You are given a car in a grid with initial state
# init = [x-position, y-position, orientation]
# where x/y-position is its position in a given
# grid and orientation is 0-3 corresponding to 'up',
# 'left', 'down' or 'right'.
#
# Your task is to compute and return the car's optimal
# path to the position specified in `goal'; where
# the costs for each motion are as defined in `cost'.

# EXAMPLE INPUT:

# grid format:
#     0 = navigable space
#     1 = occupied space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
goal = [2, 0] # final position
init = [4, 3, 0] # first 2 elements are coordinates, third is direction
#cost = [2, 1, 20] # the cost field has 3 values: right turn, no turn, left turn
cost = [2, 1, 12] # the cost field has 3 values: right turn, no turn, left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D() should return the array
# 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
#
# ----------


# there are four motion directions: up/left/down/right
# increasing the index in this array corresponds to
# a left turn. Decreasing is is a right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # do right
forward_name = ['up', 'left', 'down', 'right']

# the cost field has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']


# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D():
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))] for d in forward]

    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    policy2D[goal[0]][goal[1]] = '*'
    change = True

    while change:
        change = False

        for d in range(len(forward)):
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if goal[0] == x and goal[1] == y:
                        if value[d][x][y] > 0:
                            value[d][x][y] = 0

                            change = True

                    elif grid[x][y] == 0:
                        for a in range(len(action)):
                            d2 = (d + action[a])%len(forward)
                            newaction = forward[d2]
                            x2 = x + newaction[0]
                            y2 = y + newaction[1]

                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                v2 = value[d2][x2][y2] + cost[a]

                                if v2 < value[d][x][y]:
                                    change = True
                                    value[d][x][y] = v2


    found = False
    resign = False
    cur_pos = init
    while not found and not resign:
        x,y,d = cur_pos
        v = value[d][x][y]
        for a in range(len(action)):
            d2 = (d + action[a])%len(forward)
            newaction = forward[d2]
            x2 = x + newaction[0]
            y2 = y + newaction[1]
            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                v2 = value[d][x2][y2]
                if v2 < v:
                    policy2D[x][y] = action_name[a]
                    cur_pos = [x2,y2,d2]
            if [x2,y2] == goal:
                found = True
                break
        if cur_pos == [x,y,d]:
            # No movement, resign
            resign = True


    #for d in range(len(value)):
    #    for x in range(len(value[d])):
    #        print "[%s]" % (",".join(map(lambda x: "%3d" % x, value[d][x])))
    #    print


    return policy2D # Make sure your function returns the expected grid.

from pprint import pprint
pprint(optimum_policy2D())



