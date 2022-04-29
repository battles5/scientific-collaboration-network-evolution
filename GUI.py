# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 14:01:39 2022

@author: Orso Peruzzi

This very simple GUI is realized using the tkinter Python package.
The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit.
Both Tk and tkinter are available on most Unix platforms, including macOS, as well as on Windows systems.



"""
import matplotlib

class GUI:

    # constructor






    def __init__(self, title='Network Evolution GUI', interval=0, stepSize=1, parameterSetters=[]):

        # GUI variables inside the costructor

        self.titleText = title
        self.timeInterval = interval
        self.stepSize = stepSize
        self.parameterSetters = parameterSetters
        self.varEntries = {}
        self.statusStr = ""

        self.running = False
        self.modelFigure = None
        self.currentStep = 0

        # create the root window with tkinter



