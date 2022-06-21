# -*- coding: utf-8 -*-
"""
Created on Mon May 02 13:41:01 2022
@author: Orso Peruzzi
"""
import math
import networkx as nx
from statistics import mean


def links_node_i_at_t(t, alpha, b):
    """
    This method computes the evolution of the links' node "i" has.

       Parameters
           t : total steps of the simulation.
           alpha : ratio between the number of newly created internal links per node in unit
                time and the average number of new links that an incoming node creates.
           b : average number of new links that an incoming node creates.

       Returns:
           A list with the number of links node "i" has for each time step t.

       Raise:
           ValueError if t, alpha and b are less or equal to zero, t and b are not an integer.
    """
    if t <= 0 or alpha <= 0 or b <= 0:
        raise ValueError('Time steps, alpha and b values must be positive, but are {}, {} and {}'.format(t, alpha, b))
    if type(t) != int or type(b) != int:
        raise ValueError('t and b must be integers')
    ki = []
    ti = list(range(1, t + 1))
    for i in ti:
        v = math.floor(b * math.sqrt(t / i) * math.sqrt(((2 + alpha * t) / (2 + alpha * i)) ** 3))
        ki.append(v)
    return ki


def average_links_at_t(t, alpha, b):
    """
    This method computes the average of links per node in the network at t time steps.

       Parameters
           t : total steps of the simulation.
           alpha : ratio between the number of newly created internal links per node in unit
                time and the average number of new links that an incoming node creates.
           b : average number of new links that an incoming node creates.

       Returns:
           A list of the average number of links that each node has
           in the network at time after t steps (average links distribution at time-step t).
    """
    y = []
    i = 1
    while i <= t:
        v = links_node_i_at_t(i, alpha, b)
        ki = mean(v)
        y.append(ki)
        i += 1
    return y


def evolve(t, beta, b):
    """
    This module simulates the Barabasi-Albert model of network growth, according to preferential attachment,
            for a given time, joining rate and the number of new links that an incoming node creates.
            This also performs measurements on the network: it produces three lists containing the diameter,
            population and cluster coefficient values at each time step.

       Parameters
           t : total steps of the simulation.
           beta : new nodes' joining rate.
           b : average number of new links that an incoming node creates.

       Returns:
           Clustering coefficient, diameter and population measurements at each time step.
    """
    diameters = []
    population = []
    clustcoefficient = []
    nlist = list(range(1, (beta * t + 1), beta))
    for i in nlist:
        if b < i:
            g = nx.barabasi_albert_graph(i, b)
            i =+ 1
            c = nx.clustering(g)
            clustcoefficient.append(c[i])
            diameters.append(nx.diameter(g))
            population.append(len(g.nodes))
    return diameters, population, clustcoefficient


def kdistrubution(N, b):
    """
    This method calculates the degree distribution, P(k). The nodes join the
            system randomly at a constant rate, which implies that the "ti" values are
            uniformly distributed in time between 0 and t. The distribution function
            for the "ti" in the [0; t] interval is simply rho(t) = 1/t.

    Parameters:
        N: number of network nodes required to finish the simulation.

    Returns:
        The calculated degree distribution P(k) given all network nodes' degrees
        and a counter list of nodes to subsequently generate plots
    Raise:
        ValueError if N and b are not natural numbers.
    """
    if N <= 0 or b <= 0:
        raise ValueError('Nodes (N) and b values must be positive, but are {} and {}'.format(N, b))
    if type(N) != int or type(b) != int:
        raise ValueError('N and b must be integers')
    g = nx.barabasi_albert_graph(N, b)
    Pk = [float(j) / N for j in nx.degree_histogram(g)]
    domain = range(len(Pk))
    return Pk, domain
