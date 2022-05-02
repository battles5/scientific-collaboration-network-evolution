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
def initialize():
    global g # Defining g graph (networkx class) as a global variable
    g = nx.complete_graph(m0) # We start with a fully connected graph
    g.pos = nx.spring_layout(g) # We want to draw the graph using the nx "spring" layout for better visualization
    g.count = 0

def observe():
global g
cla()  # Cleaning axes (maybe we had a previous batch and we want to clean the graph axes)
nx.draw(g, pos=g.pos)  # Drawing the graph

def pref_select(nds):

def update():