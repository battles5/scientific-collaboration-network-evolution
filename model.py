# -*- coding: utf-8 -*-
"""
Created on Mon May 02 14:47:23 2022
@author: Orso Peruzzi
"""
import matplotlib.pyplot as plt
# import numpy as np

t = N/beta

N = list(range(1, beta * t + 1, beta))

y = average_links_at_t(t)
x = N

plt.figure(figsize=[10, 8], dpi=80, facecolor=None, edgecolor='grey')
plt.ylabel('<k>')
plt.xlabel('N')
plt.plot(x, y, color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=5)

plt.show();