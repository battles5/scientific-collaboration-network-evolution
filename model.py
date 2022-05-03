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

f = plt.figure(figsize=(20,12), dpi=300)
f.tight_layout()

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



Pk = [float(j) / N for j in nx.degree_histogram(g)]
domain = range(len(Pk))
loglog(domain, Pk, ':', label='Barabasi-Albert')
xlabel('$k$')
ylabel('$P(k)$')
legend()
show()

show(plotting_k(x, y));
