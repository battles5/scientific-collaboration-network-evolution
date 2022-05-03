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

y = fn.average_links_at_t(t, alpha, b)
x = nlist


fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('A tale of 2 subplots')

Pk = [float(j) / N for j in nx.degree_histogram(g)]
domain = range(len(Pk))
loglog(domain, Pk, ':', label='Barabasi-Albert')
xlabel('$k$')
ylabel('$P(k)$')
legend()
show()

ax1.plot(x, y, 'o-')
ax1.set_xlabel('N')
ax1.set_ylabel('<k>')

ax2.plot(x2, y2, '.-')
ax2.set_xlabel('k')
ax2.set_ylabel('P(k)')

plt.show()