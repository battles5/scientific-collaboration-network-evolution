# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:13:47 2022
@author: Orso Peruzzi
"""
import GUI
import configparser
import sys
import functions as fn
import networkx as nx

# Getting information from configuration file
config = configparser.ConfigParser()
config.read(sys.argv[1])

m0 = config.getint('settings', 'm0')  # Number of nodes in initial condition
m = config.getint('settings', 'm')  # Number of edges per new node
s = config.getint('settings', 's')  # Number of steps for growing the network
g = nx.empty_graph(n=0, create_using=None)  # Empty graph (networkx object)

# Simulation start with GUI
GUI.GUI().start(func=[fn.initialize(m0), fn.observe(g), fn.update(g, m)])
