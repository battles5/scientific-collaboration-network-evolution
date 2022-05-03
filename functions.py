# -*- coding: utf-8 -*-
"""
Created on Mon May 02 13:41:01 2022
@author: Orso Peruzzi
"""
import math
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean


def links_node_i_at_t(t, alpha, b):
    ki = []
    ti = list(range(1, t + 1))
    for i in ti:
        v = b * math.sqrt(t / i) * math.sqrt(((2 + alpha * t) / (2 + alpha * i)) ** 3)
        ki.append(v)
    return ki


def average_links_at_t(t, alpha, b):
    y = []
    i = 1
    while i <= t:
        v = links_node_i_at_t(i, alpha, b)
        ki = mean(v)
        y.append(ki)
        i += 1
    return y

def plotting_k(x, y):
    f1 = plt.figure(figsize=[10, 8], dpi=80, facecolor=None, edgecolor='grey')
    plt.ylabel('N')
    plt.xlabel('<k>')
    plt.plot(x, y, color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=5)
    return(f1)