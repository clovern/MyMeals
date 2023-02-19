from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from PlanPage import PlanPage

class AdvancedPlanPage(PlanPage):
    def __init__(self, root):
        self.createAdvancedPlanDisplay()
    
    def createAdvancedPlanDisplay(self):
        self.createUpperFrame()
        self.createTitle("Advanced Plan Creator")
        self.createLowerFrame()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for day in days:
            self.createDayPanel(day)
            # add something here to add it to the grid, at given index.

    def createDayPanel(self, day):
            self.createDayFlag(day)
            self.createTotalMealPanel()

    def createDayFlag(self, day):
        pass

    def createTotalMealPanel(self):
        self.createSingleMealPanel("Breakfast")
        self.createSingleMealPanel("Lunch")
        self.createSingleMealPanel("Dinner")

    def createSingleMealPanel(self, meal):
        pass

    def createScrollBar(self):
        pass

    def populateWidgets(self):
        pass

    def setWidgetGrid(self):
        pass



