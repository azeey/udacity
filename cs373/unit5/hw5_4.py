# --------------
# User Instructions
# 
# Define a function cte in the robot class that will
# compute the crosstrack error for a robot on a
# racetrack with a shape as described in the video.
#
# You will need to base your error calculation on
# the robot's location on the track. Remember that 
# the robot will be traveling to the right on the
# upper straight segment and to the left on the lower
# straight segment.
#
# --------------
# Grading Notes
#
# We will be testing your cte function directly by
# calling it with different robot locations and making
# sure that it returns the correct crosstrack error.  
 
from math import *
import random


# ------------------------------------------------
# 
# this is the robot class
#

class robot:

    # --------
    # init: 
    #    creates robot and initializes location/orientation to 0, 0, 0
    #

    def __init__(self, length = 20.0):
        self.x = 0.0
        self.y = 0.0
        self.orientation = 0.0
        self.length = length
        self.steering_noise = 0.0
        self.distance_noise = 0.0
        self.steering_drift = 0.0

    # --------
    # set: 
    #	sets a robot coordinate
    #

    def set(self, new_x, new_y, new_orientation):

        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation) % (2.0 * pi)


    # --------
    # set_noise: 
    #	sets the noise parameters
    #

    def set_noise(self, new_s_noise, new_d_noise):
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.steering_noise = float(new_s_noise)
        self.distance_noise = float(new_d_noise)

    # --------
    # set_steering_drift: 
    #	sets the systematical steering drift parameter
    #

    def set_steering_drift(self, drift):
        self.steering_drift = drift
        
    # --------
    # move: 
    #    steering = front wheel steering angle, limited by max_steering_angle
    #    distance = total distance driven, most be non-negative

    def move(self, steering, distance, 
             tolerance = 0.001, max_steering_angle = pi / 4.0):

        if steering > max_steering_angle:
            steering = max_steering_angle
        if steering < -max_steering_angle:
            steering = -max_steering_angle
        if distance < 0.0:
            distance = 0.0


        # make a new copy
        res = robot()
        res.length         = self.length
        res.steering_noise = self.steering_noise
        res.distance_noise = self.distance_noise
        res.steering_drift = self.steering_drift

        # apply noise
        steering2 = random.gauss(steering, self.steering_noise)
        distance2 = random.gauss(distance, self.distance_noise)

        # apply steering drift
        steering2 += self.steering_drift

        # Execute motion
        turn = tan(steering2) * distance2 / res.length

        if abs(turn) < tolerance:

            # approximate by straight line motion

            res.x = self.x + (distance2 * cos(self.orientation))
            res.y = self.y + (distance2 * sin(self.orientation))
            res.orientation = (self.orientation + turn) % (2.0 * pi)

        else:

            # approximate bicycle model for motion

            radius = distance2 / turn
            cx = self.x - (sin(self.orientation) * radius)
            cy = self.y + (cos(self.orientation) * radius)
            res.orientation = (self.orientation + turn) % (2.0 * pi)
            res.x = cx + (sin(res.orientation) * radius)
            res.y = cy - (cos(res.orientation) * radius)

        return res




    def __repr__(self):
        return '[x=%.5f y=%.5f orient=%.5f]'  % (self.x, self.y, self.orientation)


############## ONLY ADD / MODIFY CODE BELOW THIS LINE ####################
    # Starting location is (0,radius)
    def cte(self, radius):
        cte = 0
        # Case 1, left side, center (radius,radius)
        if self.x < radius:
            cte = sqrt((radius - self.x)**2 + (radius - self.y)**2) - radius
            #print "CTE=",cte
        # Case 2, top side
        elif self.x >= radius and self.x < 3*radius and self.y >= radius:
           cte =  self.y - 2*radius
        # Case 3, right side, center (3*radius, radius)
        elif self.x >= 3*radius:
            cte = sqrt((3*radius - self.x)**2 + (radius - self.y)**2) - radius
        #Case 4, bottom side
        else:
            cte = -self.y

        return cte
    
############## ONLY ADD / MODIFY CODE ABOVE THIS LINE ####################


import pylab as plt
def plot(path,label=None):
    pathcopy=[list(p) for p in path]
    #pathcopy.append(path[0])
    x,y = zip(*pathcopy)
    plt.plot(x,y,'.-',label=label)
    plt.grid()
    plt.show(block=False)


# ------------------------------------------------------------------------
#
# run - does a single control run.


N = 2000
def run(params, radius, printflag = False):
    myrobot = robot()
    myrobot.set(0.5, radius, pi / 2.0)
    speed = 1.0 # motion distance is equal to speed (we assume time = 1)
    err = 0.0
    int_crosstrack_error = 0.0

    crosstrack_error = myrobot.cte(radius) # You need to define the cte function!

    # Ideal path
    path = []
    for i in range(N):
       if i <= N/4:
           x = radius * cos(i*pi/(float(N)/4) + pi/2 ) + radius
           y = radius * sin(i*pi/(float(N)/4) + pi/2 ) + radius
       elif i < N/2:
           x = radius + (2.*radius/(N/4.)*(i - N/4))
           y = 0
       elif i < 3*N/4:
           x = radius * cos(i*pi/(float(N)/4) + 3*pi/2 ) + 3*radius
           y = radius * sin(i*pi/(float(N)/4) + 3*pi/2 ) + radius
       else:
           x = 3*radius - (2.*radius/(N/4.)*(i - 3*N/4))
           y = 2*radius
       path.append((x,y))

    plot(path,label='Ideal Path')


    coords = []

    #for i in range(N*2):
    for i in range(int(2*N)):
        diff_crosstrack_error = - crosstrack_error
        crosstrack_error = myrobot.cte(radius)
        diff_crosstrack_error += crosstrack_error
        int_crosstrack_error += crosstrack_error
        steer = - params[0] * crosstrack_error \
                - params[1] * diff_crosstrack_error \
                - params[2] * int_crosstrack_error
        myrobot = myrobot.move(steer, speed)
        if i >= N:
            err += crosstrack_error ** 2
        if printflag:
            #print myrobot, "CTE=",crosstrack_error,"steer=",steer
            coords.append((myrobot.x,myrobot.y))
    if printflag:
        plot(coords,label='Robot Path')
    return err / float(N)

radius = 25.0
params = [10.0, 15.0, 0]
err = run(params, radius, True)
print '\nFinal paramaeters: ', params, '\n ->', err


plt.legend(loc='best')
plt.title('CS373 Robot motion given ideal path( radius=%f, params=%s, error=%f, N=%d)' % (radius,str(params), err,N))
plt.show()
