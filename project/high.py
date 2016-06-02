# -*- coding: cp950 -*-
from visual import *
from random import random # random module for generate random numbers
from visual.graph import *
import csv

N = 50 # number of the He atoms
L = ((24.4E-3/(6E23))*N)**(1/3.0)/2 # side 

#length of the cubic container box
m,size = 4E-3/6E23, 310E-12 # He atoms mass, radius are made 10 times bigger for easiear collision
L_size = L-size # L – size, used many times in the program
k, T = 1.38E-23, 10000.0 # k = Boltzmann constant, and T = temperature in unit K
t, dt = 0, 0.5E-13 # dt = 0.5E-13 second
vrms = (3*k*T/m)**0.5 # root mean square velocity at T
atoms = [] # list to contain the 50 atoms

# histogram initialization, more on this see http://vpython.org/contents/docs/graph.html
deltav = 300.
vdist = gdisplay(x=800, y=0, ymax = N*0.08,width=500, height=300, xtitle='v', ytitle='dN')
theory = gcurve(color=color.cyan) # This line and the following 3 are to plot the theoretical speed distribution
dv = 10.
for v in arange(0.,17001.+dv,dv):
    theory.plot(pos=(v,(deltav/dv)*N*4.*pi*((m/(2.*pi*k*T))**1.5)*exp((-0.5*m*v**2)/(k*T))*v**2*dv))
observation = ghistogram(bins=arange(0.,17000.,deltav),accumulate=1, average=1, color=color.red) # setup for histogram

with open("high.csv","r") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            rate(10000)
            #print (row)
    #calculate new positions for all atoms and plot histogram
            observation.plot(data=[ float(i) for i in row])
    #### and then you will calculate the momentum transferred to the walls and obtain the resulted pressure
    #### print the averaged pressure on the walls every 1000*dt
