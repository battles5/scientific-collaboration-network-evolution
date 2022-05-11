# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 08:09:18 2022

@author: Orso Peruzzi
"""
import hypothesis
from hypothesis import strategies as st
from hypothesis import settings
from hypothesis import given

import functions
import model
import configuration
import numpy as np


@given(t = st.integers(1, configuration.t), alpha = st.floats(), b = st.integers(1, configuration.b))
@settings(max_examples = 1)
def test_links_node_i_at_t(t, alpha, b):
    assume(alpha > 0)
    # Declaring an empty list for the links of node i
    ki = []

    ti = list(range(1, t + 1))
    for i in ti:
        v = b * math.sqrt(t / i) * math.sqrt(((2 + alpha * t) / (2 + alpha * i)) ** 3)
        ki.append(v)
    return ki
