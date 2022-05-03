# -*- coding: utf-8 -*-
"""
Created on Mon May 02 14:47:23 2022
@author: Orso Peruzzi
"""
import functions as fn
import configparser
import networkx as nx
from pylab import *

DEFAULTS = "configuration.txt"
config = configparser.ConfigParser()
config.read(DEFAULTS)

a = config.getfloat('settings', 'a')
beta = config.getint('settings', 'beta')
b = config.getint('settings', 'b')
N = config.getint('settings', 'N')
g = nx.barabasi_albert_graph(N, 5)
alpha = a/b
t = N/beta
nlist = list(range(1, int(beta * t + 1), int(beta)))

x1 = nlist
y1 = fn.average_links_at_t(t, alpha, b)

Pk = [float(j) / N for j in nx.degree_histogram(g)]
domain = range(len(Pk))

x2 = domain
y2 = Pk

fig =  plt.figure(figsize=[8, 6], dpi=80, facecolor=None, edgecolor='grey')

ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(x1, y1, color='brown', lw=1.5)
ax1.set_xlabel('$N$')
ax1.set_ylabel('$<k>$')

ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(x2, y2, color='purple', lw=1.5)
ax2.set_xlabel('$k$')
ax2.set_ylabel('$P(k)$')
# ax2.set_yscale('log')