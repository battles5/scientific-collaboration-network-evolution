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

@given(t = st.integers(), alpha = st.floats(), b = st.integers(0, b))
@settings(max_examples = 1, suppress_health_check=HealthCheck.all())
def test_links_node_i_at_t(t, alpha, b):
    # Claculating a list of the number of links node i has for each time step t
    ki = fn.links_node_i_at_t(t, alpha, b)
    # Test if the number of links node i has at t is t
    assert len(ki) == t
    # Test if the list contains ordered numbers
    # ki_sorted = sort(ki)
    # assert ki == ki_sorted
    # Test if the list contains only positive numbers
    # for i in range(len(ki)):
    #         assert ki[i] > 0

if __name__ == "main":
    pass