# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:13:47 2022
@author: Orso Peruzzi
"""
import GUI
from pylab import *
import networkx as nx
import configparser

# Getting information from configuration.txt file
DEFAULTS = "configuration.txt"
config = configparser.ConfigParser()
config.read(DEFAULTS)

m0 = config.getint('settings', 'm0') # Number of nodes in initial condition
m = config.getint('settings', 'm') # Number of edges per new node
s = config.getint('settings', 's') # Number of steps for growing the network

# -----------------------------------
# Main functions of the network simulation
# -----------------------------------
# ------ Step 1/4 ------
def initialize():
    # Defining g graph (networkx class) as a global variable
    global g
    # We start with a fully connected graph
    g = nx.complete_graph(m0)
    # We want to draw the graph using the nx "spring" layout for better visualization
    g.pos = nx.spring_layout(g)
    g.count = 0

# ------ Step 2/4 ------
def observe():
    global g
    # Cleaning axes (maybe we had a previous batch and we want to clean the graph axes)
    cla()
    # Drawing the graph
    nx.draw(g, pos=g.pos)

# ------ Step 3/4 ------
# This function is used to select nodes based on the preferential attachment criterion.
def pref_select(nds):
    global g
    # Generating random value between 0 and the sum of all node's degree
    r = uniform(0, sum([g.degree(i) for i in nds]))
    x = 0
    # Now we choose randomly a node to connect with.
    # According to preferential attachment the higher the degree of the node,
    # the more chances to choose it.
    for i in nds:
        x += g.degree(i)
        if r <= x:
            return i

# ------ Step 4/4 ------
def update():
    global g
    g.count += 1
    # The network grows once in every s steps
    if g.count % 20 == 0:
        # Creating a list of all graph's nodes and defining a new coming node
        nds = list(g.nodes)
        newcomer = max(nds) + 1
        # We connect the newcomer(s) node to the graph
        for i in range(m):
            j = pref_select(nds)
            g.add_edge(newcomer, j)
            nds.remove(j)
        g.pos[newcomer] = (0, 0)
    # Simulation of node movement
    g.pos = nx.spring_layout(g, pos=g.pos, iterations=3)


# -----------------------------------
# Simulation start with GUI
# -----------------------------------
GUI.GUI().start(func=[initialize, observe, update])