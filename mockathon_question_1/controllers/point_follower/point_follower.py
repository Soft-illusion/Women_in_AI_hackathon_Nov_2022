#!/usr/bin/env python3
from controller import Robot
from controller import GPS , Motor ,  InertialUnit
import math

## ------------------------------------------------------------------------
#Edit here 

def point_follower(current,goal):
    # Impelement a Controller to reach the goal.

    # current is <x,y,theta>
    # goals is <x,y,theta>
    # leftSpeed is a float
    # rightSpeed is a float


    leftSpeed = 1.0
    rightSpeed = 1.0
    # Sample velocities provided to make robot mopve straight. 
    return leftSpeed,rightSpeed

def Sketch():
    # Use this function to calculate points to follow trace a curve 
    # Optional function you can also impelement everything in point_follower function.
    goal = [0,0,0] # [x,y,theta]
    return goal

## ------------------------------------------------------------------------

#Initializing robot to access sensor from the robot.
robot = Robot()
timestep = int(robot.getBasicTimeStep()) # Defined timestep (in msec) to enable sensors and define sensor frequency.

# Enable GPS to get X,Y 
gps = robot.getGPS("gps")
gps.enable(timestep) # Enabled GPS sensor to get x, y, z location at time difference equat to timestep.

# Enable IMU to get theta
imu = robot.getInertialUnit("imu")
imu.enable(timestep) # Enabled GPS sensor to get theta location at time difference equat to timestep.


# Enable Wheels
wheels_names = ["wheel1", "wheel2", "wheel3", "wheel4"]
wheels = []
for i in range(4):
    wheels.append(robot.getMotor(wheels_names[i]))
    wheels[-1].setPosition(float('inf')) # setting max position limit of each wheel to infinity to convert it to velocity mode 
    wheels[-1].setVelocity(0.0) # Setting zero velocity for all the wheels.

if __name__=="__main__":
    while robot.step(timestep) != -1:

        # x,y,theta
        current = [gps.getValues()[0],gps.getValues()[1],imu.getRollPitchYaw()[2]]    
        print(current)
        goal = [0,0,0] # initial goal to initialize goal array

        ## ------------------------------------------------------------------------
        #Edit here 
        # *Use Sketch function to calculate points to trace the curve
        # Use point_follower controller to trace the curve.  
        # point_follower should return leftSpeed and rightSpeed 
        leftSpeed,rightSpeed = point_follower(current,goal)
        ## ------------------------------------------------------------------------

        # Setting velocities to each wheel based on calculation.
        wheels[0].setVelocity(leftSpeed) # Front left wheel
        wheels[1].setVelocity(rightSpeed) # Front right wheel
        wheels[2].setVelocity(leftSpeed) # Rear left wheel
        wheels[3].setVelocity(rightSpeed) # Rear right wheel
         
