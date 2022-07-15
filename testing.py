# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 08:09:18 2022
@author: Orso Peruzzi
"""
from hypothesis import strategies as st
from hypothesis import settings
from hypothesis import given
from hypothesis import HealthCheck
from numpy import sort
import functions as fn
import networkx as nx

b = 10
m0 = 5


@given(t = st.integers(min_value = 1),
        alpha = st.floats(min_value = 0, exclude_min = True),
        b = st.integers(1, b))
@settings(max_examples = 1, suppress_health_check = HealthCheck.all())
def test_links_node_i_at_t(t, alpha, b):
    # Calculating a list of the number of links node i has for each time step t
    ki = fn.links_node_i_at_t(t, alpha, b)
    # Test if the number of links node i has at t is t
    assert len(ki) == t
    # Test if the list contains ordered numbers
    ki_sorted = sort(ki)
    assert ki == ki_sorted
    # Test if the list contains only natural numbers
    for i in range(len(ki)):
        assert ki[i] > 0
        assert isinstance(ki[i], int) == True

@given(t = st.integers(min_value = 1),
        alpha = st.floats(min_value = 0, exclude_min = True),
        b = st.integers(1, b))
@settings(max_examples = 1, suppress_health_check = HealthCheck.all())
def test_average_links_at_t(t, alpha, b):
    # A list of the average number of links that each node has in the
    # network at time after t steps
    avg_links_distribution = fn.links_node_i_at_t(t, alpha, b)
    # Test if the number of links node i has at t is t
    assert len(avg_links_distribution) == t
    # Test if the list contains ordered numbers
    ald_sorted = sort(avg_links_distribution)
    assert avg_links_distribution == ald_sorted
    # Test if the list contains only positive numbers
    for i in range(len(avg_links_distribution)):
        assert avg_links_distribution[i] > 0

@given(t = st.integers(min_value = 1),
        beta = st.integers(min_value = 1),
        b = st.integers(1, b))
@settings(max_examples = 1, suppress_health_check = HealthCheck.all())
def test_evolve(t, beta, b):
    diameters, population, clustcoefficient = fn.evolve(t, beta, b)
    # Test if population increases and remains positive
    for i in range(len(population)):
        assert population[i] <= (population[i-1]) and population[i] > 0
        # Test if population's "i" element is an integer
        assert isinstance(population[i], int)
    # Test if diameter increases and remains positive
    for i in range(len(diameters)):
        assert diameters[i] <= (diameters[i - 1]) and diameters[i] > 0
        # Test if diameters' "i" element is an integer
        assert isinstance(diameters[i], int)
    # Test if diameter increases and remains positive
    for i in range(len(clustcoefficient)):
        assert clustcoefficient[i] > 0

@given(N = st.integers(min_value = b),
        b = st.integers(1, b))
@settings(max_examples = 1, suppress_health_check = HealthCheck.all())
def test_kdistrubution(N, b):
    Pk, domain = fn.kdistrubution(N, b)
    # Test if domain increases and remains positive
    assert len(domain) > 0
    # Test if distribution Pk and the domain have the same lenght
    assert len(Pk) == len(domain)
    # Test if Pk distribution is normalized
    assert sum(Pk) == 1

@given(m0 = st.integers(min_value = 2))
@settings(max_examples = 1, suppress_health_check = HealthCheck.all())
def test_initialize(m0):
    g = fn.initialize(m0)
    # Test if is a networkx graph
    assert type(g) == nx.classes.graph.Graph
    # The "spring" layout is represented in networkx as a dictionary of dimension "m0"
    # Test if g.pos instance is a dict with m0 elements inside
    assert type(g.pos) == dict
    assert len(g.pos) == m0

@given(m0 = st.integers(min_value = 2))
@settings(max_examples = 1, suppress_health_check = HealthCheck.all())
def test_pref_select(g, nds):
    g = nx.complete_graph(m0)
    nds = list(g.nodes)
    node_list = []
    # Test if the node "i" is not the same after a step
    # Test if the node "i" is a natural number > 0
    for i in range(len(nds)):
        node_i = fn.pref_select(g, nds)
        node_list.append(node_i)
        assert node_i > 0
        assert isinstance(node_i, int) == True
        if i > 0:
            assert node_list[i-1] != node_list[i]

@given(m0 = st.integers(min_value = 2), m = st.integers(min_value = 1, max_value = 3))
@settings(max_examples = 1, suppress_health_check = HealthCheck.all())
def test_update(m, m0):
    g = nx.complete_graph(m0)
    graph = fn.update(g, m)
    # Test if is a networkx graph
    assert type(graph) == nx.classes.graph.Graph
    # Test if update function increases the number of nodes
    graph_1 = fn.update(g, m)
    assert nx.nodes(graph) < nx.nodes(graph_1)
