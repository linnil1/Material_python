from random import random # random module for generate random numbers
import csv
from math import pi,sin,cos,sqrt

N = 50 # number of the He atoms
L = ((24.4E-3/(6E23))*N)**(1/3.0)/2 # side length of the cubic container box
m,size = 4E-3/6E23, 310E-12 # He atoms mass, radius are made 10 times bigger for easiear collision
L_size = L-size # L – size, used many times in the program
k, T = 1.38E-23, 100.0 # k = Boltzmann constant, and T = temperature in unit K
t, dt = 0, 0.5E-13 # dt = 0.5E-13 second
vrms = (3*k*T/m)**0.5 # root mean square velocity at T
atoms = [] # list to contain the 50 atoms

dv = 10.

class vector:
    def __init__ (self,x,y,z):
        self.x,self.y,self.z = x,y,z

    def __mul__(self,d):
        return vector(self.x*d,self.y*d,self.z*d)
    def __sub__(self,v2):
        return vector(self.x-v2.x,self.y-v2.y,self.z-v2.z)
    def __add__(self,v2):
        return vector(self.x+v2.x,self.y+v2.y,self.z+v2.z)

class particle:
    pass

def mag(a):
    return sqrt( a.x*a.x + a.y*a.y + a.z*a.z)
def dot(a,b):
    return ( a.x*b.x + a.y*b.y + a.z*b.z)

def init(myK,name):
    global T,vrms,atoms
    T = myK
    vrms = (3*k*T/m)**0.5 # root mean square velocity at T
    atoms = []
    data = list( csv.reader(open(name,"r")))
    for i in range(N):
        atom = particle()
        atom.pos = vector(float(data[i*2][0]),float(data[i*2][1]),float(data[i*2][2]))
        atom.m,atom.v = m,vector(float(data[i*2+1][0]),float(data[i*2+1][1]),float(data[i*2+1][2]))
        atoms.append(atom)
    
def vcollision(a1,a2): # function to find the velocities of atoms after each collision
    v1prime = a1.v - (a1.pos-a2.pos)* (2. * a2.m/(a1.m+a2.m) * dot (a1.v-a2.v, a1.pos-a2.pos) / mag(a1.pos-a2.pos)**2)
    v2prime = a2.v - (a2.pos-a1.pos)* (2. * a1.m/(a1.m+a2.m) * dot (a2.v-a1.v, a2.pos-a1.pos) / mag(a2.pos-a1.pos)**2) 
    a1.v,a2.v =  v1prime, v2prime 

def main():
    #calculate new positions for all atoms and plot histogram
    for atom in atoms:
        atom.pos = atom.pos +  atom.v * dt
#### find collisions between walls, and then handle their collision,
    for atom in atoms:
        if abs(atom.pos.x) >= L:
            atom.v.x *= -1
        if abs(atom.pos.y) >= L:
            atom.v.y *= -1
        if abs(atom.pos.z) >= L:
            atom.v.z *= -1
#### find collisions between atoms, and then handle their collisions
    for i in  range(N):
        for j in  range(N):
            if i!=j and mag(atoms[i].pos-atoms[j].pos)<2*size:
                vcollision(atoms[i],atoms[j])

def mystr(a):
    return [a.x,a.y,a.z]

myKmult=1
for i in range(1,6):
    name = "/tmp/pvnrt/data_{0}K_ball.csv".format(myKmult)
    init(myKmult,name)
    name = "/tmp/pvnrt/data_{0}K.csv".format(myKmult)
    writer = csv.writer(open(name, 'a'))
    for count in range(70000):
        v=[]
        for i in range(N): #### calculate new positions for atoms
            v.append(round(mag(atoms[i].v),3))
        writer.writerow(v)
        for c in range(4):
            main()
    name = "/tmp/pvnrt/data_{0}K_ball.csv".format(myKmult)
    writer = csv.writer(open(name, 'w'))
    for i in range(N):
        writer.writerow(mystr(atoms[i].pos))
        writer.writerow(mystr(atoms[i].v))
    myKmult *= 10
#### and then you will calculate the momentum transferred to the walls and obtain the resulted pressure
#### print the averaged pressure on the walls every 1000*dt
