"""
Verlet time integration of a particle in a gravitational potential.
Produces a plot of the trajectory in the xy plane, potential energy against time
and an output file.
"""
 
import numpy as np
import matplotlib.pyplot as pyplot
from Particle3D import Particle3D
import math
import sys
 
#Read name of output file from command line
if len(sys.argv)!=2:
    print "Wrong number of arguments"
    print "Usage: " +sys.argv[0] + " <output file>"
    quit()
else:
    outfileName = sys.argv[1]
 
#Part to read in the file containing particle data
#First attach file handle to input file
file_handle = open("Pluto","r")
 
#Read particle data from file
p = Particle3D.from_file(file_handle)
 
#Open output file for writing
outfile = open(outfileName, "w")
 
#Set up simulation parameters
mp = p.mass
numstep = 1000
time = 0.0
dt = 0.01
 
#Set up force and potential energy equations
force = -(mp*p.position)/(math.sqrt(p.position[0]**2 + p.position[1]**2 + p.position[2]**2))**3
Uenergy = -mp/(math.sqrt(p.position[0]**2 + p.position[1]**2 + p.position[2]**2))
 
#Set up Kinetic Energy using the method defined in Particle3D
KineticEnergy = p.kineticEnergy()
 
 
#Set up total energy
TotEnergy = Uenergy + KineticEnergy
 
 
#Set up data lists
x_posValue = [p.position[0]]
y_posValue = [p.position[1]]
t_Value = [time]
TotalE = [TotEnergy]
 
 
outfile.write("{0:f} {1:f}\n".format(p.position[0], p.position[1]))
 
#Start time integration loop
 
for i in range(numstep):
 
    #Update particle position
    p.leapPos2nd(dt, force)
 
    #Update force
    force_new = -(mp*p.position)/math.sqrt(p.position[0]**2 + p.position[1]**2 + p.position[2]**2)**3
 
    #Update particle velocity, based on average of current and new force
    p.leapVelocity(dt, 0.5*(force + force_new))
 
    #Update potential energy
    Uenergy = -mp/(math.sqrt(p.position[0]**2 + p.position[1]**2 + p.position[2]**2))
     
 
    #Update Total Energy
    TotEnergy = Uenergy + KineticEnergy
     
    #Reset force variable
    force = force_new
 
    #Increase time
    time = time + dt
 
    #Output particle information
    t_Value.append(time)
    x_posValue.append(p.position[0])
    y_posValue.append(p.position[1])
    TotalE.append(TotEnergy)
    outfile.write("{0:f} {1:f} {2:f}\n".format(time, p.position[0], p.position[1]))
 
#Close output file
outfile.close()
 
#Plot graphs of xy Trajectory and Total Energy vs time
pyplot.plot(x_posValue,y_posValue)
pyplot.title("Trajectory in X-Y Plane")
pyplot.xlabel("X-Value")
pyplot.ylabel("Y-Label")
pyplot.show()
pyplot.plot(t_Value,TotalE)
pyplot.title("Total Energy vs Time")
pyplot.xlabel("Time")
pyplot.ylabel("Total Energy")
pyplot.show()
