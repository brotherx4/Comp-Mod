import sys
import numpy as np
class Particle3D(object):

    # Initialise a Particle3D instance
    def __init__(self, pos, vel, mass, label):
        self.position = pos
        self.velocity = vel
        self.mass = mass
	self.label = label

    # Formatted output as String
    def __str__(self):
        return "label = " + str(self.label) + "x = " + str(self.position[0]) + "y = " + str(self.position[1]) + "z = " + str(self.position[2])

    # Kinetic energy
    def kineticEnergy(self):
        Magvel = np.linalg.norm(self.velocity)
        return 0.5*self.mass*(Magvel**2)

    # Time integration methods
    # First-order velocity update
    def leapVelocity(self, dt, force):
        self.velocity = self.velocity + dt*(force/self.mass)

    # First-order position update
    def leapPos1st(self, dt):
        self.position = self.position + dt*self.velocity

    # Second-order position update
    def leapPos2nd(self, dt, force):
        self.position = self.position + dt*self.velocity + 0.5*dt**2*force/self.mass

    # Static Method reading a file to create a particle
    @staticmethod
    def from_file(file_handle):
        line = file_handle.readline()
        tokens = line.split()
        pos = np.array([float(tokens[0]), float(tokens[1]), float(tokens[2])])
        vel = np.array([float(tokens[3]), float(tokens[4]), float(tokens[5])])
        mass = float(tokens[6])
        label = tokens[7]
        return Particle3D(pos, vel, mass, label)

    # Static Method returning relative vector separation of two particles
    @staticmethod
    def separation(p1,p2):
        separation = p1.position-p2.position
        return separation
