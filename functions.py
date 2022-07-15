# -*- coding: utf-8 -*-
"""
Created on Mon May 02 13:41:01 2022
@author: Orso Peruzzi
"""
import math
import networkx as nx
from statistics import mean
from pylab import cla, uniform, random

random.seed = 42


# -----------------------------------
# Functions of the model simulation
# -----------------------------------
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
            c = nx.average_clustering(g)
            clustcoefficient.append(c)
            diameters.append(nx.diameter(g))
            population.append(len(g.nodes))
            i = + 1
    return clustcoefficient, diameters, population


def kdistrubution(N, b):
    """
    This method calculates the degree distribution, P(k). The nodes join the
        system randomly at a constant rate, which implies that the "ti" values are
        uniformly distributed in time between 0 and t. The distribution function
        for the "ti" in the [0; t] interval is simply rho(t) = 1/t.

        Parameters:
            b : average number of new links that an incoming node creates.
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


# -----------------------------------
# Functions of the network simulation
# -----------------------------------
def initialize(m0):
    """
    This method initializes the system by instantiating a complete graph and setting
    a "spring" layout.
    It also sets the counter of time steps at zero value.

       Parameters
           m0 : Number of nodes in initial condition.

       Returns:
           The initialized graph g with chosen layout and counter step value.
    """
    # We start with a fully connected graph
    g = nx.complete_graph(m0)
    # We want to draw the graph using the nx "spring" layout for better visualization
    # so we set it with .pos method
    g.pos = nx.spring_layout(g)
    g.count = 0
    return g


def observe(g):
    """
    This method cleans the axes of the precedent batch (if them are still present)
    and draws the graph using the layout defined before.

        Parameters
            g : the networkx graph that is being processed in the evolution simulation.
    """
    # Cleaning axes (maybe we had a previous batch, and we want to clean the graph axes)
    cla()
    # Drawing the graph
    nx.draw(g, pos=g.pos)


def pref_select(g, nds):
    """
    This method selects a node to connect with the incoming one
    based on the preferential attachment criterion.

        Parameters
            nds : list of the graph's nodes.
            g : the networkx graph that is being processed in the evolution simulation.

        Returns:
            The chosen node to connect with.
    """
    # Generating random value between 0 and the sum of all node's degree
    r = uniform(0, sum([g.degree(i) for i in nds]))
    x = 0
    # Now we choose randomly a node to connect with.
    # According to preferential attachment the higher the degree of the node,
    # the more chances to choose it.
    for i in nds:
        x += g.degree(i)
        if r <= x:
            return i


def update(g, m):
    """
    this method updates the counter and system state by adding m link(s) to a new node
    according to the preferential attachment criterion. It then generates and draws
    the new network layout by placing the new node in (0, 0).
    Finally, it generates a new network layout and reproduces the layout again to make
    the representation dynamic and avoid overlapping between nodes.

        Parameters
            g : the networkx graph that is being processed in the evolution simulation.
            m : the number of edges per new node.

        Returns:
            The graph updated to the next state in the evolution of the system.
    """
    g.count += 1
    # The network grows once in every s steps
    if g.count % 20 == 0:
        # Creating a list of all graph's nodes and defining a new coming node
        nds = list(g.nodes)
        newcomer = max(nds) + 1
        # We connect the newcomer(s) node to the graph
        for i in range(m):
            j = pref_select(nds)
            g.add_edge(newcomer, j)
            nds.remove(j)
        g.pos[newcomer] = (0, 0)
    # Simulation of node movement
    g.pos = nx.spring_layout(g, pos=g.pos, iterations=3)
    return g
