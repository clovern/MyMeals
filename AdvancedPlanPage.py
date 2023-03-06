from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from PlanPage import PlanPage

class AdvancedPlanPage(PlanPage):
    def __init__(self, root, outer):
        # super().__init__(root)
        self.outer = outer
        self.createAdvancedPlanDisplay()
    
    def createAdvancedPlanDisplay(self):
        self.createUpperFrame()
        self.createLowerFrame()
        self.createTitle("Advanced Plan Creator")
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        index = 0
        for day in days:
            self.createDayPanel(day, index)
            index += 1
            # add something here to add it to the grid, at given index.

    def createDayPanel(self, day, index):
            self.dayFrame= ttk.Frame(self.lowercontent)
            self.dayFrame['padding'] = (10, 10, 10, 10)
            self.dayFrame.grid(column=0, row=index)
            self.createDayFlag(day)
            self.createSingleMealPanel("Breakfast", 1)
            self.createSingleMealPanel("Lunch", 2)
            self.createSingleMealPanel("Dinner", 3)

    def createDayFlag(self, day):
        self.dayFlag = ttk.Label(self.dayFrame, text=day, width=20, font=("Arial", 15))
        self.dayFlag.grid(column=0, row=0)

    def createSingleMealPanel(self, meal, index):
        self.mealLabel = ttk.Label(self.dayFrame, text=meal, padding=(20,2,20,2))
        self.mealLabel.grid(column=1, row=index)
        self.createMealDropdown()
        self.advancedDropdown.grid(column=2, row=index)
    
    def createMealDropdown(self):
            self.choiceSelection = StringVar()
            self.advancedDropdown = ttk.Combobox(self.dayFrame, textvariable=self.choiceSelection)
            self.advancedDropdown['values'] = ('None',
                             'Vegan',
                             'Vegetarian',
                             'Chicken',
                             'Pork',
                             'Beef',
                             'Turkey',
                             'Seafood',
                             'Reheats-well',
                             '$',
                             '$$',
                             '$$$')
            self.advancedDropdown.current(0)

    def createScrollBar(self):
        pass

    def populateWidgets(self):
        pass

    def setWidgetGrid(self):
        pass



