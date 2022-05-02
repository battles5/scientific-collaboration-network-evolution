# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 14:01:39 2022

@author: Orso Peruzzi
"""
# This very simple dinamic and interactive GUI is realized using the Python 3.9 inbuilt tkinter package.
# The tkinter package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit.
#
# Project website:
# https://docs.python.org/3/library/tkinter.html
#
# I decided to create a GUI to have control over the simulation as it runs
# and for an easier visualization.
import matplotlib
import warnings
import platform

# Suppressing matplotlib deprecation warnings
# Updated 02/05/2022
warnings.filterwarnings("ignore", category = matplotlib.cbook.MatplotlibDeprecationWarning)

# System check (added later)
# Updated 02/05/2022
if platform.system() == 'Windows':
    backend = 'TkAgg'
else:  # SM 3/28/2020
    backend = 'Qt5Agg'
matplotlib.use(backend)



class GUI:

    # Constructor
    def __init__(self, title='Network Evolution GUI', interval=0, stepSize=1, parameterSetters=[]):

        # GUI variables inside the costructor

        # General project variables (such as main title, ...)
        self.titleText = title
        self.timeInterval = interval
        self.stepSize = stepSize
        self.parameterSetters = parameterSetters
        self.varEntries = {}
        self.statusStr = ""

        # Default status for GUI controls
        self.running = False
        self.modelFigure = None
        self.currentStep = 0

        # Root window with tkinter
        self.rootWindow = Tk()
        self.statusText = StringVar(self.rootWindow, value=self.statusStr)  # at this point, statusStr =

        # Graphic default settings
        self.rootWindow.wm_title(self.titleText)  # titleText = 'PyCX Simulator'
        self.rootWindow.protocol('WM_DELETE_WINDOW', self.quitGUI)
        self.rootWindow.geometry('450x250')
        self.rootWindow.columnconfigure(0, weight=1)
        self.rootWindow.rowconfigure(0, weight=1)
        self.notebook = Notebook(self.rootWindow)
        self.notebook.pack(side=TOP, padx=2, pady=2)

        # Frames
        self.frameRun = Frame(self.rootWindow)
        self.frameSettings = Frame(self.rootWindow)
        self.notebook.add(self.frameRun, text="Run")
        self.notebook.add(self.frameSettings, text="Settings")
        self.status = Label(self.rootWindow, width=40, height=3, relief=SUNKEN, bd=1, textvariable=self.statusText)
        self.status.pack(side=TOP, fill=X, padx=5, pady=5, expand=NO)

        # There will be two frames: Run and Settings.
        # Below there is the variables list and default settings for
        # each frames.

        # -----------------------------------
        # frameRun
        # -----------------------------------
        # buttonRun
        self.runPauseString = StringVar(self.rootWindow)  # added "self.rootWindow" by Hiroki Sayama 10/09/2018
        self.runPauseString.set("Run")
        self.buttonRun = Button(self.frameRun, width=30, height=2, textvariable=self.runPauseString, command=self.runEvent)
        self.buttonRun.pack(side=TOP, padx=5, pady=5)

        # buttonStep
        self.buttonStep = Button(self.frameRun, width=30, height=2, text='Step Once', command=self.stepOnce)
        self.buttonStep.pack(side=TOP, padx=5, pady=5)

        # buttonReset
        self.buttonReset = Button(self.frameRun, width=30, height=2, text='Reset', command=self.resetModel)
        self.buttonReset.pack(side=TOP, padx=5, pady=5)

        # -----------------------------------
        # frameSettings
        # -----------------------------------
        can = Canvas(self.frameSettings)

        lab = Label(can, width=25, height=1, text="Step size ", justify=LEFT, anchor=W, takefocus=0)
        lab.pack(side='left')

        self.stepScale = Scale(can, from_=1, to=50, resolution=1, command=self.changeStepSize, orient=HORIZONTAL,
                               width=25, length=150)
        self.stepScale.set(self.stepSize)
        self.stepScale.pack(side='left')

        can.pack(side='top')

        can = Canvas(self.frameSettings)
        lab = Label(can, width=25, height=1, text="Step visualization delay in ms ", justify=LEFT, anchor=W,
                    takefocus=0)
        lab.pack(side='left')
        self.stepDelay = Scale(can, from_=0, to=max(2000, self.timeInterval),
                               resolution=10, command=self.changeStepDelay, orient=HORIZONTAL, width=25, length=150)
        self.stepDelay.set(self.timeInterval)
        # self.showHelp(self.stepDelay, "The visualization of each step is delays by the given number of milliseconds.")
        self.stepDelay.pack(side='left')

        can.pack(side='top')

    # Function that defines the new status of the system at any start.
    def setStatusStr(self, newStatus):
        self.statusStr = newStatus
        self.statusText.set(self.statusStr)

    # ------ Model control functions for changing parameters ------
    # This let the user decide how many time steps the simulation
    # run before it is upgraded.
    def changeStepSize(self, val):
        self.stepSize = int(val)

    # This function let the user decide the upgrading frequency
    # of the visualization, setting the temporal
    # interval in ms.
    def changeStepDelay(self, val):
        self.timeInterval = int(val)

    # This function sets the chosen parameters and saves them.
    def saveParametersCmd(self):
        for variableSetter in self.parameterSetters:
            variableSetter(float(self.varEntries[variableSetter].get()))
            self.setStatusStr("New parameter values have been set")

    # This function sets the chosen parameters and saves them as
    # initial conditions in order to start the simulation.
    # It reset the initial condition invoking "resetModel()".
    def saveParametersAndResetCmd(self):
        self.saveParametersCmd()
        self.resetModel()

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
    # This function calls and makes the modelStepFunc function working for a time step.
    # This function is envoked when runEvent is active.
    def stepModel(self):
        if self.running:
            self.modelStepFunc()
            self.currentStep += 1
            self.setStatusStr("Step " + str(self.currentStep))
            self.status.configure(foreground='black')
            if (self.currentStep) % self.stepSize == 0:
                self.drawModel()
            self.rootWindow.after(int(self.timeInterval * 1.0 / self.stepSize), self.stepModel)

    # ------ stepOnce ------
    # This function calls and makes the modelStepFunc function working for just a single time step.
    # This function is envoked when "Step Once" button is clicked.
    def stepOnce(self):
        self.running = False
        self.runPauseString.set("Continue Run")
        self.modelStepFunc()
        self.currentStep += 1
        self.setStatusStr("Step " + str(self.currentStep))
        self.drawModel()
        if len(self.parameterSetters) > 0:
            self.buttonSaveParameters.configure(state=NORMAL)

    # ------ resetModel ------
    # This function interrupts and takes the model to initial conditions.
    # This function is envoked when "Reset" button is clicked.
    def resetModel(self):
        self.running = False
        self.runPauseString.set("Run")
        self.modelInitFunc()
        self.currentStep = 0;
        self.setStatusStr("Model has been reset")
        self.drawModel()

    # ------ drawModel ------
    # This function activates the visualization window and shows the simulation state.
    # If the visualization windows is already open it shows the simulation state.
    def drawModel(self):
        plt.ion()  # SM 3/26/2020
        if self.modelFigure == None or self.modelFigure.canvas.manager.window == None:
            self.modelFigure = plt.figure()
        self.modelDrawFunc()
        self.modelFigure.canvas.manager.window.update()
        plt.show()

    # ------ start ------
    # This executes the "initialize", "observe" and "update" model functions taking them as arguments.
    # This function is envoked at every execution.
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

    # ------ quitGUI ------
    # This function quit the graphic user interface and close all windows.
    def quitGUI(self):
        self.running = False
        self.rootWindow.quit()
        plt.close('all')
        self.rootWindow.destroy()

        widget.bind("<Enter>", lambda e: setText(self))
        widget.bind("<Leave>", lambda e: showHelpLeave(self))