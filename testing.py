# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 08:09:18 2022

@author: Orso Peruzzi
"""
import hypothesis
from hypothesis import strategies as st
from hypothesis import settings
from hypothesis import given
from hypothesis import HealthCheck
from numpy import sort

import functions as fn
import model
import configparser
import numpy as np
import math
from statistics import mean

# Getting information from configuration.txt file
DEFAULTS = "configuration.txt"
config = configparser.ConfigParser()
config.read(DEFAULTS)

b = config.getint('settings', 'b')


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