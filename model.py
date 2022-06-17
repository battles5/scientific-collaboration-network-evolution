# -*- coding: utf-8 -*-
"""
Created on Mon May 02 14:47:23 2022
@author: Orso Peruzzi
"""
import functions as fn
import configparser
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

path = config.get('paths','path')

alpha = a / b
t = int(N / beta)

# -----------------------------------
# Main
# -----------------------------------
# ------ First part ------
# Here the evolution calculated before is repeated for
# different values of b in order to investigate different
# behaviors at different scales.
# Preferential attachment is calculated according to beta and b chosen values.
# Networkx is used to create and make evolve the graph.

for i in range(b, b + 10, 2):
    if i == b:
        diameters0, population0, clustcoefficient0 = fn.evolve(t, beta, i)
    if i == b+2:
        diameters1, population1, clustcoefficient1 = fn.evolve(t, beta, i)
    if i == b+4:
        diameters2, population2, clustcoefficient2 = fn.evolve(t, beta, i)
    if i == b+6:
        diameters3, population3, clustcoefficient3 = fn.evolve(t, beta, i)
    if i == b+8:
        diameters4, population4, clustcoefficient4 = fn.evolve(t, beta, i)

# ------ Second part ------
# In this part the network's connectivity k and
# its distribution are calculated.

k_average = fn.average_links_at_t(t, alpha, b)
Pk, domain = fn.kdistrubution(N, b)


# -----------------------------------
# Plotting part
# -----------------------------------
# Here, a figure with 4 subplots is generated.

x1 = list(range(1, (beta * t + 1), beta))
y1 = k_average

x2 = domain
y2 = Pk

x3 = population0
y3 = diameters0

x4 = population0
y4 = clustcoefficient0

x5 = population1
y5 = clustcoefficient1

x6 = population2
y6 = clustcoefficient2

x7 = population3
y7 = clustcoefficient3

x8 = population4
y8 = clustcoefficient4

fig = plt.figure(figsize=[10, 10], dpi=80, facecolor=None, edgecolor='grey')
plt.style.use('seaborn')

# ------ Subplot 1 ------
# <k> in function of N
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(x1, y1, color='grey', lw=1.5)
ax1.scatter(x1, y1, cmap="Blues", s=80, alpha=0.6, edgecolor='black', linewidth=1)
ax1.set_xlabel('$N$', fontsize=15)
ax1.set_ylabel('$<k>$', fontsize=15)

# ------ Subplot 2 ------
# Connectivity distribution, ln scaled.
ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(x2, y2, color='grey', lw=1.5)
ax2.scatter(x2, y2, cmap="Blues", s=80, alpha=0.6, edgecolor='black', linewidth=1)
ax2.set_xlabel('$ln$ $k$', fontsize=15)
ax2.set_ylabel('$ln$ $P(k)$', fontsize=15)
ax2.get_xaxis().set_major_formatter(
    matplotlib.ticker.LogFormatter(base=e, labelOnlyBase=True,
                                   minor_thresholds=None, linthresh=None))
ax2.get_yaxis().set_major_formatter(
    matplotlib.ticker.LogFormatter(base=e, labelOnlyBase=True,
                                   minor_thresholds=None, linthresh=None))

# ------ Subplot 3 ------
# Diameters values in function of N.
ax3 = fig.add_subplot(2, 2, 3)
ax3.scatter(x3, y3, cmap="Blues", s=80, alpha=0.6, edgecolor='black', linewidth=1)
ax3.set_xlabel('$N$', fontsize=15)
ax3.set_ylabel('$d$', fontsize=15)

# ------ Subplot 4 ------
# Cluster coefficients in function of N.
ax4 = fig.add_subplot(2, 2, 4)
ax4.scatter(x4, y4, cmap="Blues", s=80, alpha=0.6, edgecolor='black', linewidth=1)
ax4.scatter(x5, y5, cmap="Blues", s=80, alpha=0.6, edgecolor='black', linewidth=1)
ax4.scatter(x6, y6, cmap="Blues", s=80, alpha=0.6, edgecolor='black', linewidth=1)
ax4.scatter(x7, y7, cmap="Blues", s=80, alpha=0.6, edgecolor='black', linewidth=1)
ax4.scatter(x8, y8, cmap="Blues", s=80, alpha=0.6, edgecolor='black', linewidth=1)
ax4.set_xlabel('$N$', fontsize=15)
ax4.set_ylabel('$C$', fontsize=15)

fig.savefig(path)
