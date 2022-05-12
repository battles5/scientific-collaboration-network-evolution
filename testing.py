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
import functions
import model
import configparser
import numpy as np
import math

# Getting information from configuration.txt file
DEFAULTS = "configuration.txt"
config = configparser.ConfigParser()
config.read(DEFAULTS)

b = config.getint('settings', 'b')

@given(t = st.integers(), alpha = st.floats(), b = st.integers(0, b))
@settings(max_examples = 1, suppress_health_check=HealthCheck.all())
def test_links_node_i_at_t(t, alpha, b):
    hypothesis.assume(alpha > 0)
    hypothesis.assume(t > 0)
    hypothesis.assume(b > 0)
    # Declaring an empty list for the links of node i.
    ki = []
    # Declaring a list with t ordered time steps.
    ti = list(range(1, t + 1))
    # Do a cycle in order to calculate the number of links of node i for each time step.
    for i in ti:
        # Calculate the result of the master equation given the parameters.
        v = b * math.sqrt(t / i) * math.sqrt(((2 + alpha * t) / (2 + alpha * i)) ** 3)
        # Test if the result of master equation is always positive.
        # assert v > 0
        # Add the resault to the links list.
        ki.append(v)
        # Test if the calculated value is different from the previous one.
        if i > 2:
            assert ki[i-1] != v
    # Test if the number of elements in the links list is actually the same of time steps.
    assert len(ki) == len(ti)
    return ki


if __name__ == "main":
    pass






