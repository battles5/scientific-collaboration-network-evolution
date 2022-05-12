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
    """This method computes the evolution of the links node i has can be.

       Parameters
           t : total steps of the simulation.
           alpha : ratio between the number of newly created internal links per node in unit
                time and the average number of new links that an incoming node creates.
           b : average number of new links that an incoming node creates.

       Returns:
           The number of links node i has at the time step t.

       Raise:
           ValueError if t, alpha and b are less or equal to zero, t and b are not a integer."""
    if t <= 0 or alpha <= 0 or b <= 0:
        raise ValueError('Time steps, alpha and b values must be positive, but are {}, {} and {}'.format(t, alpha, beta))
    if type(t) != int or type(b) != int:
        raise ValueError('t and b must be integers')
    ki = []
    ti = list(range(1, t + 1))
    for i in ti:
        v = b * math.sqrt(t / i) * math.sqrt(((2 + alpha * t) / (2 + alpha * i)) ** 3)
        ki.append(v)
    return ki


def average_links_at_t(t, alpha, b):
    """This method computes the average of links per node in the network at t time steps.

       Parameters
           t : total steps of the simulation.
           alpha : ratio between the number of newly created internal links per node in unit
                time and the average number of new links that an incoming node creates.
           b : average number of new links that an incoming node creates.

       Returns:
           The average number of links that each node has in the network at time after t steps.

       Raise:
           ValueError if t, alpha and b are less or equal to zero or t and b are not a integer."""
    if t <= 0 or alpha <= 0 or b <= 0:
        raise ValueError('Time steps, alpha and b values must be positive, but are {}, {} and {}'.format(t, alpha, beta))
    if type(t) != int or type(b) != int:
        raise ValueError('t and b must be integers')
    y = []
    i = 1
    while i <= t:
        v = links_node_i_at_t(i, alpha, b)
        ki = mean(v)
        y.append(ki)
        i += 1
    return y