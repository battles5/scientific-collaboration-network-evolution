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

DEFAULTS = "configuration.txt"
config = configparser.ConfigParser()
config.read(DEFAULTS)

a = config.getfloat('settings', 'a')
beta = config.getint('settings', 'beta')
b = config.getint('settings', 'b')
N = config.getint('settings', 'N')
g = nx.barabasi_albert_graph(N, b)
alpha = a/b
t = N/beta
nlist = list(range(1, int(beta * t + 1), int(beta)))

x1 = nlist
y1 = fn.average_links_at_t(t, alpha, b)

Pk = [float(j) / N for j in nx.degree_histogram(g)]
domain = range(len(Pk))

x2 = domain
y2 = Pk

fig =  plt.figure(figsize=[12, 6], dpi=80, facecolor=None, edgecolor='grey')

ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(x1, y1, color='brown', lw=1.5)
ax1.set_xlabel('$N$', fontsize = 15)
ax1.set_ylabel('$<k>$', fontsize = 15)

ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(x2, y2, color = 'purple', lw = 1.5)
ax2.set_xlabel('$ln$ $k$', fontsize = 15)
ax2.set_ylabel('$ln$ $P(k)$', fontsize = 15)
ax2.get_xaxis().set_major_formatter(
    matplotlib.ticker.LogFormatter(base=e, labelOnlyBase=True,
                                   minor_thresholds=None, linthresh=None))
ax2.get_yaxis().set_major_formatter(
    matplotlib.ticker.LogFormatter(base=e, labelOnlyBase=True,
                                   minor_thresholds=None, linthresh=None))
