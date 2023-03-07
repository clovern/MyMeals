from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from PlanPage import PlanPage

class AdvancedPlanPage(PlanPage):
    def __init__(self, root, outer):
        self.outer = outer
        self.createAdvancedPlanDisplay()
    
    def createAdvancedPlanDisplay(self):
        self.createUpperFrame()
        self.createLowerFrame()
        self.createLowerLeftFrame()
        self.createLowerRightFrame()
        self.createTitle("Advanced Plan Creator")
        self.createAllDays()
        self.createSubmitButton()
    
    def createLowerLeftFrame(self):
        self.lowerLeftContent = ttk.Frame(self.lowercontent, height=550, width=400)
        self.lowerLeftContent.grid(column=0, row=0)
        self.lowerLeftContent.grid_propagate(0)
    
    def createLowerRightFrame(self):
        self.lowerRightContent = ttk.Frame(self.lowercontent, height=550, width=400)
        self.lowerRightContent.grid(column=1, row=0)
        self.lowerRightContent.grid_propagate(0)
    
    def createAllDays(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        index = 0
        for day in days:
            self.createDayPanel(day, index)
            index += 1

    def createDayPanel(self, day, index):
        if (index < 4):
            self.dayFrame= ttk.Frame(self.lowerLeftContent)
        else:
            self.dayFrame= ttk.Frame(self.lowerRightContent)
            index -= 4
        
        self.dayFrame['padding'] = (10, 10, 10, 10)
        self.dayFrame.grid(column=0, row=index)
        self.createDayFlag(day)
        self.createSingleMealPanel("Breakfast", 1)
        self.createSingleMealPanel("Lunch", 2)
        self.createSingleMealPanel("Dinner", 3)

    def createDayFlag(self, day):
        self.dayFlag = ttk.Label(self.dayFrame, text=day, width=10, font=("Arial", 15))
        self.dayFlag.grid(column=0, row=0)

    def createSingleMealPanel(self, meal, index):
        self.mealLabel = ttk.Label(self.dayFrame, text=meal, padding=(20,2,20,2))
        self.mealLabel.grid(column=1, row=index)
        self.createMealDropdown()
        self.advancedDropdown.grid(column=2, row=index)
    
    def createMealDropdown(self):
            self.choiceSelection = StringVar()
            self.advancedDropdown = ttk.Combobox(self.dayFrame, textvariable=self.choiceSelection)
            self.advancedDropdown['values'] = (
                             'Exclude this meal',
                             'None',
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
    
    def createSubmitButton(self):
        super().createSubmitButton()
        self.submitButton.grid(column=0, columnspan=3, row=1)


    def generatePlan(self):
        pass



