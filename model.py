# -*- coding: utf-8 -*-
"""
Created on Mon May 02 14:47:23 2022
@author: Orso Peruzzi
"""
import functions as fn
import configparser

DEFAULTS = "configuration.txt"
config = configparser.ConfigParser()
config.read(DEFAULTS)

a = config.getfloat('settings', 'a')
beta = config.getint('settings', 'beta')
b = config.getint('settings', 'b')
N = config.getint('settings', 'N')

alpha = a/b
t = N/beta
N = list(range(1, int(beta * t + 1), int(beta)))

y = fn.average_links_at_t(t, alpha, b)
x = N

fn.plotting(x, y, 'N', '<k>')