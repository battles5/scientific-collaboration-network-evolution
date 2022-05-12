# -*- coding: utf-8 -*-
"""
Created on Mon May 02 14:47:23 2022
@author: Orso Peruzzi
"""
import functions as fn
import configparser
import networkx as nx
from pylab import *
from math import e
from matplotlib import pyplot as plt

# Getting information from configuration.txt file
DEFAULTS = "configuration.txt"
config = configparser.ConfigParser()
config.read(DEFAULTS)

a = config.getfloat('settings', 'a')
beta = config.getint('settings', 'beta')
b = config.getint('settings', 'b')
N = config.getint('settings', 'N')
alpha = a/b
t = int(N/beta)
nlist = list(range(1, int(beta * t + 1), int(beta)))

# -----------------------------------
# Main part
# -----------------------------------
# ------ First part ------
# Initialization and computation of the evolution of the network.
# Preferential attachment is calculated according to beta and b chosen values.
# Networkx is used to create and make evolve the graph.
diameters = []
population = []
clustcoefficient1 = []
for i in nlist:
    if b < i:
        g = nx.barabasi_albert_graph(i, b)
        i =+ 1
        c1 = nx.clustering(g)
        clustcoefficient1.append(c1[i])
        diameters.append(nx.diameter(g))
        population.append(len(g.nodes))

# ------ Second part ------
# Here the evolution calculated before is repeated for
# different values of b in order to investigate different
# behaviors at different scales.
b1 = 2
clustcoefficient2 = []
clustcoefficient3 = []
clustcoefficient4 = []
clustcoefficient5 = []
population2 = []
population3 = []
population4 = []
population5 = []
for i in range(2, 10, 2):
    if i == 2:
        for j in nlist:
            if i < j:
                g = nx.barabasi_albert_graph(j, i)
                j = + 1
                c2 = nx.clustering(g)
                clustcoefficient2.append(c2[j])
                population2.append(len(g.nodes))
    if i == 4:
        for j in nlist:
            if i < j:
                g = nx.barabasi_albert_graph(j, i)
                j = + 1
                c3 = nx.clustering(g)
                clustcoefficient3.append(c3[j])
                population3.append(len(g.nodes))
    if i == 6:
        for j in nlist:
            if i < j:
                g = nx.barabasi_albert_graph(j, i)
                j = + 1
                c4 = nx.clustering(g)
                clustcoefficient4.append(c4[j])
                population4.append(len(g.nodes))
    if i == 8:
        for j in nlist:
            if i < j:
                g = nx.barabasi_albert_graph(j, i)
                j = + 1
                c5 = nx.clustering(g)
                clustcoefficient5.append(c5[j])
                population5.append(len(g.nodes))

# ------ Third part ------
# In this part the network's connectivity k and
# its distribution are calculated.
kaverage = fn.average_links_at_t(t, alpha, b)

Pk = [float(j) / N for j in nx.degree_histogram(g)]
domain = range(len(Pk))

# -----------------------------------
# Plotting part
# -----------------------------------
# Here, a figure with 4 subplots is generated.
x1 = nlist
y1 = kaverage

x2 = domain
y2 = Pk

x3 = population
y3 = diameters

x4 = population
y4 = clustcoefficient1

x5 = population2
y5 = clustcoefficient2

x6 = population3
y6 = clustcoefficient3

x7 = population4
y7 = clustcoefficient4

x8 = population5
y8 = clustcoefficient5

fig =  plt.figure(figsize=[10, 10], dpi=80, facecolor=None, edgecolor='grey')
plt.style.use('seaborn')

# ------ Subplot 1 ------
# <k> in function of N
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(x1, y1, color='grey', lw=1.5)
ax1.scatter(x1, y1, cmap="Blues", s=100, alpha=0.6, edgecolor='black', linewidth=1)
ax1.set_xlabel('$N$', fontsize = 15)
ax1.set_ylabel('$<k>$', fontsize = 15)

# ------ Subplot 2 ------
# Connectivity distribution, ln scaled.
ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(x2, y2, color = 'grey', lw = 1.5)
ax2.scatter(x2, y2, cmap="Blues", s=100, alpha=0.6, edgecolor='black', linewidth=1)
ax2.set_xlabel('$ln$ $k$', fontsize = 15)
ax2.set_ylabel('$ln$ $P(k)$', fontsize = 15)
ax2.get_xaxis().set_major_formatter(
    matplotlib.ticker.LogFormatter(base=e, labelOnlyBase=True,
                                   minor_thresholds=None, linthresh=None))
ax2.get_yaxis().set_major_formatter(
    matplotlib.ticker.LogFormatter(base=e, labelOnlyBase=True,
                                   minor_thresholds=None, linthresh=None))

# ------ Subplot 3 ------
# Diameter value in function of N.
ax3 = fig.add_subplot(2, 2, 3)
ax3.scatter(x3, y3, cmap="Blues", s=100, alpha=0.6, edgecolor='black', linewidth=1)
ax3.set_xlabel('$N$', fontsize = 15)
ax3.set_ylabel('$d$', fontsize = 15)

# ------ Subplot 1 ------
# Cluster coefficient in function of N.
ax4 = fig.add_subplot(2, 2, 4)
ax4.scatter(x4, y4, cmap="Blues", s=100, alpha=0.6, edgecolor='black', linewidth=1)
ax4.scatter(x5, y5, cmap="Blues", s=100, alpha=0.6, edgecolor='black', linewidth=1)
ax4.scatter(x6, y6, cmap="Blues", s=100, alpha=0.6, edgecolor='black', linewidth=1)
ax4.scatter(x7, y7, cmap="Blues", s=100, alpha=0.6, edgecolor='black', linewidth=1)
ax4.set_xlabel('$N$', fontsize = 15)
ax4.set_ylabel('$C$', fontsize = 15)

tight_layout()