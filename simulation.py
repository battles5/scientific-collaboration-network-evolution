# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:13:47 2022

@author: Orso Peruzzi
"""
import GUI
from pylab import *
import networkx as nx

m0 = 5  # Number of nodes in initial condition
m = 1  # Number of edges per new node

# Main functions of the network simulation

# ------ Step 1/4 ------
def initialize():
    global g # Defining g graph (networkx class) as a global variable
    g = nx.complete_graph(m0) # We start with a fully connected graph
    g.pos = nx.spring_layout(g) # We want to draw the graph using the nx "spring" layout for better visualization
    g.count = 0

# ------ Step 2/4 ------
def observe():
global g
cla()  # Cleaning axes (maybe we had a previous batch and we want to clean the graph axes)
nx.draw(g, pos=g.pos)  # Drawing the graph

# ------ Step 3/4 ------
def pref_select(nds):
    global g
    r = uniform(0, sum([g.degree(i) for i in nds])) # Random choice of nodes
    x = 0
    for i in nds:
        x += g.degree(i)
        if r <= x:
            return i
