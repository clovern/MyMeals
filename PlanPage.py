from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from abc import ABC, abstractmethod

class PlanPage(ABC):
    def __init__(self, root):
        root.title("MyMeals")
        self.createUpperFrame()
        self.createLowerFrame()

    def createUpperFrame(self):
        self.uppercontent = ttk.Frame(self.outer).grid(column=0, row=0)
    
    def createLowerFrame(self):
        self.lowercontent = ttk.Frame(self.outer).grid(column=0, row=1)

    # FIXME implement
    def createNavBar(self):
        pass

    # FIXME implement
    def createTitle(self, stringVal):
        pass

    # FIXME implement
    def createPlanButton():
        pass

    # FIXME implement
    def generatePlan():
        pass

    @abstractmethod
    def populateWidgets(self):
        ...

    @abstractmethod
    def setWidgetGrid(self):
        ...
    
    def clearPage(self):
        self.uppercontent.destroy()
        self.lowercontent.destroy()