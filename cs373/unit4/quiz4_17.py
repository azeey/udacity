# ----------
# User Instructions:
# 
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal. 
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

#grid = [[0, 1, 0, 0, 0, 0],
        #[0, 1, 0, 0, 0, 0],
        #[0, 1, 0, 0, 0, 0],
        #[0, 1, 0, 0, 0, 0],
        #[0, 0, 0, 0, 1, 0]]

grid = [[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------

def compute_value():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    calc=[]
    def get_value(cell):
        x,y  = cell
        calc.append(cell)
        if cell == goal:
            print "Reached goal", cell
            value[x][y] = 0
            return 0
        else:
            tmp_value = []
            for i in range(len(delta)):
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                    #if grid[x2][y2] == 0 and closed[x2][y2] == 0:
                        #closed[x2][y2] = 1
                        #v = get_value([x2,y2])
                        #tmp_value.append(v)
                    if grid[x2][y2] == 0 and closed[x2][y2] == 0:
                        if [x2,y2] != goal:
                            closed[x2][y2] = 1
                        v = get_value([x2,y2])
                        tmp_value.append(v)


            print (x,y),tmp_value,
            if len(tmp_value) == 0:
                v = 0
            else:
                v = max(tmp_value) + 1
                value[x][y] = v
            print v
            return v
            #print (x,y),tmp_value
            #if len(tmp_value) == 0:
                #return 0
            #else:
                #v = min(tmp_value) + 1
                ##print v
                #value[x][y] = v
                #return v



    get_value(init)

    return value #make sure your function returns a grid of values as demonstrated in the previous video.

#def compute_value():
#    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
#    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
#    closed[init[0]][init[1]] = 1
#    value[goal[0]][goal[1]] = 0

#    x = init[0]
#    y = init[1]
#    g = 0

#    open = [[g, x, y]]

#    def get_value(cell):
#        g,x,y = cell
#        if [x,y] == goal:
#            print "Reached goal", cell
#            value[x][y] = 0
#            return 0
#        else:
#            calc=[]
#            for i in range(len(delta)):
#                x2 = x + delta[i][0]
#                y2 = y + delta[i][1]
#                if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
#                    #if grid[x2][y2] == 0 and closed[x2][y2] == 0:
#                        #closed[x2][y2] = 1
#                        #v = get_value([x2,y2])
#                        #tmp_value.append(v)
#                    if  closed[x2][y2] == 0 and grid[x2][y2] == 0 :
#                        g2 = g + cost_step
#                        open.append([g2,x2,y2])
#                        closed[x2][y2] = 1

#            print open
#            tmp_value = []
#            while len(open) > 0:
#                open.sort()
#                open.reverse()
#                next = open.pop()
#                v = get_value(next) + 1
#                print "V:",next, v

#            ##print (x,y),tmp_value,
#            #if len(tmp_value) == 0:
#            #    return 0
#            #v = min(tmp_value) + 1
#            ##print v
#            #value[x][y] = v
#            #return v
#            return 0



#    get_value(open[0])

#    return value #make sure your function returns a grid of values as demonstrated in the previous video.

from pprint import pprint
pprint(compute_value())
pprint(grid)
