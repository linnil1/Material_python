from visual import *
from random import random # random module for generate random numbers
from visual.graph import *

N = 50 # number of the He atoms
L = ((24.4E-3/(6E23))*N)**(1/3.0)/2 # side length of the cubic container box
m,size = 4E-3/6E23, 310E-12 # He atoms mass, radius are made 10 times bigger for easiear collision
L_size = L-size # L – size, used many times in the program
k, T = 1.38E-23, 298.0 # k = Boltzmann constant, and T = temperature in unit K
t, dt = 0, 0.5E-13 # dt = 0.5E-13 second
vrms = (3*k*T/m)**0.5 # root mean square velocity at T
atoms = [] # list to contain the 50 atoms

# histogram initialization, more on this see http://vpython.org/contents/docs/graph.html
deltav = 100.
vdist = gdisplay(x=800, y=0, ymax = N*deltav/1000.,width=500, height=300, xtitle='v', ytitle='dN')
theory = gcurve(color=color.cyan) # This line and the following 3 are to plot the theoretical speed distribution
dv = 10.
for v in arange(0.,3001.+dv,dv):
    theory.plot(pos=(v,(deltav/dv)*N*4.*pi*((m/(2.*pi*k*T))**1.5)*exp((-0.5*m*v**2)/(k*T))*v**2*dv))
observation = ghistogram(bins=arange(0.,3000.,deltav),accumulate=1, average=1, color=color.red) # setup for histogram

# initialization of display, setting up for the random position distribution and random velocity direction of atoms
scene = display(width=800, height=800,background=(0.2,0.2,0))
container = box(length = 2*L, height = 2*L, width = 2*L, opacity=0.2, color = color.yellow )
for i in range(N):
    position = vector(-L_size+2*L_size*random(),-L_size+2*L_size*random(),-L_size+2*L_size*random())
    if i== N-1:
        atom = sphere(pos=position, radius = size, color=color.yellow, make_trail = True, retain = 600)
    else:
        atom = sphere(pos=position, radius = size, color=(random(), random(), random()))
    ra, rb = pi*random(), 2*pi*random()
    atom.m, atom.v = m, vector(vrms*sin(ra)*cos(rb), vrms*sin(ra)*sin(rb), vrms*cos(ra))
    atoms.append(atom)
    
def vcollision(a1,a2): # function to find the velocities of atoms after each collision
    v1prime = a1.v - 2 * a2.m/(a1.m+a2.m) *(a1.pos-a2.pos) * dot (a1.v-a2.v, a1.pos-a2.pos) / abs(a1.pos-a2.pos)**2
    v2prime = a2.v - 2 * a1.m/(a1.m+a2.m) *(a2.pos-a1.pos) * dot (a2.v-a1.v, a2.pos-a1.pos) / abs(a2.pos-a1.pos)**2
    a1.v,a2.v =  v1prime, v2prime

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
#### and then you will calculate the momentum transferred to the walls and obtain the resulted pressure
#### print the averaged pressure on the walls every 1000*dt
