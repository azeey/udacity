colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = []

def init_distrib(world):
    ''' Initialize p with a uniform distribution--state of maximum confusion '''
    global p
    count = 0
    for row in world:
        count += len(row)

    for row in world:
        tmp = [1./count] * len(row)
        p.append(tmp)

def sum2d(q):
    return sum(map(sum,q))

def normalize(q):
    s = float(sum2d(q))
    for i in range(len(q)):
        for j in range(len(q[i])):
            q[i][j] /= s
    return q

def sense(p,Z):
    ''' Computes the posterior probabilty of the world after a sensor reading'''
    q = []
    for i in range(len(p)):
        q_tmp = []
        for j in range(len(p[i])):
            if Z == colors[i][j]:
                q_tmp.append(p[i][j]*sensor_right)
            else:
                q_tmp.append(p[i][j]*(1 - sensor_right))
        q.append(q_tmp)

    # Normalize distribution
    q = normalize(q)
    return q

def move(p,U):
    ''' Computes the posterior probabilty of the world after a move.
    Movement commands are:
       [0,0]  = No move
       [0,1]  = Right
       [0,-1] = Left
       [1,0]  = Down
       [-1,0] = Up
    '''
    # Special case
    if U == [0,0]:
        return p

    q = []
    for i in range(len(p)):
        q_tmp = []
        for j in range(len(p[i])):
            s = p[i][j]*(1-p_move) # Failed to move
            s += p[(i - U[0]) % len(p)][j]*(p_move * abs(U[0])) # Vertical motion
            s += p[i][(j - U[1]) % len(p[i])]*(p_move * abs(U[1]))# Horizontal motion
            q_tmp.append(s)
        q.append(q_tmp)

    return q

init_distrib(colors)
for i in range(len(motions)):
    p = move(p,motions[i])
    p = sense(p,measurements[i])

#Your probability array must be printed 
#with the following code.

show(p)





