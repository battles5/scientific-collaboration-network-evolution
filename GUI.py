# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 14:01:39 2022

@author: Orso Peruzzi
"""
# This very simple GUI is realized using the Python 3.9 inbuilt tkinter package.
# The tkinter package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit.
#
# Project website:
# https://docs.python.org/3/library/tkinter.html
#
# I decided to create a GUI to have control over the simulation as it runs
# and for an easier visualization.

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

        # root window with tkinter
        self.rootWindow = Tk()
        self.statusText = StringVar(self.rootWindow, value=self.statusStr)  # at this point, statusStr =


    # ------ runEvent ------
    # This event is envoked when "Run" button is clicked.
    def runEvent(self):
        self.running = not self.running
        if self.running:
            self.rootWindow.after(self.timeInterval, self.stepModel)
            self.runPauseString.set("Pause")
            self.buttonStep.configure(state=DISABLED)
            self.buttonReset.configure(state=DISABLED)
            if len(self.parameterSetters) > 0:
                self.buttonSaveParameters.configure(state=NORMAL)
                self.buttonSaveParametersAndReset.configure(state=DISABLED)
        else:
            self.runPauseString.set("Continue Run")
            self.buttonStep.configure(state=NORMAL)
            self.buttonReset.configure(state=NORMAL)
            if len(self.parameterSetters) > 0:
                self.buttonSaveParameters.configure(state=NORMAL)
                self.buttonSaveParametersAndReset.configure(state=NORMAL)

    # ------ stepModel ------
    # This function calls and makes the simulation working
    def stepModel(self):
        if self.running:
            self.modelStepFunc()
            self.currentStep += 1
            self.setStatusStr("Step " + str(self.currentStep))
            self.status.configure(foreground='black')
            if (self.currentStep) % self.stepSize == 0:
                self.drawModel()
            self.rootWindow.after(int(self.timeInterval * 1.0 / self.stepSize), self.stepModel)

    def stepOnce(self):
        self.running = False
        self.runPauseString.set("Continue Run")
        self.modelStepFunc()
        self.currentStep += 1
        self.setStatusStr("Step " + str(self.currentStep))
        self.drawModel()
        if len(self.parameterSetters) > 0:
            self.buttonSaveParameters.configure(state=NORMAL)

    def resetModel(self):
        self.running = False
        self.runPauseString.set("Run")
        self.modelInitFunc()
        self.currentStep = 0;
        self.setStatusStr("Model has been reset")
        self.drawModel()

    def drawModel(self):
        plt.ion()  # SM 3/26/2020
        if self.modelFigure == None or self.modelFigure.canvas.manager.window == None:
            self.modelFigure = plt.figure()
        self.modelDrawFunc()
        self.modelFigure.canvas.manager.window.update()
        plt.show()

    def start(self, func=[]):
        if len(func) == 3:
            self.modelInitFunc = func[0]
            self.modelDrawFunc = func[1]
            self.modelStepFunc = func[2]
            if (self.modelStepFunc.__doc__ != None and len(self.modelStepFunc.__doc__) > 0):
                self.showHelp(self.buttonStep, self.modelStepFunc.__doc__.strip())
            if (self.modelInitFunc.__doc__ != None and len(self.modelInitFunc.__doc__) > 0):
                self.textInformation.config(state=NORMAL)
                self.textInformation.delete(1.0, END)
                self.textInformation.insert(END, self.modelInitFunc.__doc__.strip())
                self.textInformation.config(state=DISABLED)

            self.modelInitFunc()
            self.drawModel()
        self.rootWindow.mainloop()

    def quitGUI(self):
        self.running = False
        self.rootWindow.quit()
        plt.close('all')
        self.rootWindow.destroy()

    def showHelp(self, widget, text):
        def setText(self):
            self.statusText.set(text)
            self.status.configure(foreground='blue')

        def showHelpLeave(self):
            self.statusText.set(self.statusStr)
            self.status.configure(foreground='black')

        widget.bind("<Enter>", lambda e: setText(self))
        widget.bind("<Leave>", lambda e: showHelpLeave(self))