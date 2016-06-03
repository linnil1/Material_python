# -*- coding: cp950 -*-
from visual import *
from random import random # random module for generate random numbers
from visual.graph import *
import csv

Kname = 100

N = 50 # number of the He atoms
L = ((24.4E-3/(6E23))*N)**(1/3.0)/2 # side 

#length of the cubic container box
m,size = 4E-3/6E23, 310E-12 # He atoms mass, radius are made 10 times bigger for easiear collision
L_size = L-size # L – size, used many times in the program
k, T = 1.38E-23, 1.*Kname # k = Boltzmann constant, and T = temperature in unit K
t, dt = 0, 0.5E-13 # dt = 0.5E-13 second
vrms = (3*k*T/m)**0.5 # root mean square velocity at T
atoms = [] # list to contain the 50 atoms

# histogram initialization, more on this see http://vpython.org/contents/docs/graph.html
deltav = 60.
vdist = gdisplay(x=800, y=0, ymax = N*deltav/1000.+2,width=500, height=300, xtitle='v', ytitle='dN')
theory = gcurve(color=color.cyan) # This line and the following 3 are to plot the theoretical speed distribution
dv = 10.
for v in arange(0.,3001.+dv,dv):
    theory.plot(pos=(v,(deltav/dv)*N*4.*pi*((m/(2.*pi*k*T))**1.5)*exp((-0.5*m*v**2)/(k*T))*v**2*dv))
observation = ghistogram(bins=arange(0.,3000.,deltav),accumulate=1, average=1, color=color.red) # setup for histogram

with open("data_"+str(Kname)+"K.csv","r") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        rate(10000)
        observation.plot(data=[ float(i) for i in row])

# initialization of display, setting up for the random position distribution and random velocity direction of atoms
scene = display(width=800, height=800,background=(0.2,0.2,0))
container = box(length = 2*L, height = 2*L, width = 2*L, opacity=0.2, color = color.yellow )
def open_last():
    with open("data_"+str(Kname)+"K_ball.csv","r") as csvFile:
        reader = list(csv.reader(csvFile))
        for i in range(N):
            position = vector(float(reader[i*2][0]),float(reader[i*2][1]),float(reader[i*2][2]))
            if i== N-1:
                atom = sphere(pos=position, radius = size, color=color.yellow, make_trail = True, retain = 600)
            else:
                atom = sphere(pos=position, radius = size, color=(random(), random(), random()))
            atom.m, atom.v = m, vector(float(reader[i*2+1][0]),float(reader[i*2+1][1]),float(reader[i*2+1][2]))
            atoms.append(atom)

    
def vcollision(a1,a2): # function to find the velocities of atoms after each collision
    v1prime = a1.v - 2 * a2.m/(a1.m+a2.m) *(a1.pos-a2.pos) * dot (a1.v-a2.v, a1.pos-a2.pos) / abs(a1.pos-a2.pos)**2
    v2prime = a2.v - 2 * a1.m/(a1.m+a2.m) *(a2.pos-a1.pos) * dot (a2.v-a1.v, a2.pos-a1.pos) / abs(a2.pos-a1.pos)**2
    a1.v,a2.v =  v1prime, v2prime
    
open_last()
while True:
    t += dt
    rate(10000)

#calculate new positions for all atoms and plot histogram
    v=[]
    for i in range(N):
    #### calculate new positions for atoms
        v.append(mag(atoms[i].v))
    observation.plot(data=v)
    for atom in atoms:
        atom.pos += atom.v * dt
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


