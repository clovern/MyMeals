from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from PlanPage import PlanPage
from MealInfoDisplay import MealInfoDisplay

class AdvancedPlanPage(PlanPage):
    def __init__(self, root, outer):
        self.outer = outer
        super().__init__()
        self.dropdownDict = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [],
                        "Friday": [], "Saturday": [], "Sunday": []}
        self.createAdvancedPlanDisplay()
    
    def createAdvancedPlanDisplay(self):
        self.createLowerLeftFrame()
        self.createLowerRightFrame()
        self.createTitle("Advanced Plan Creator")
        self.createAllDays()
        self.createSubmitButton()

    def createDayPanel(self, day, index):
        super().createDayPanel(day, index)
        self.createSingleMealPanel("Breakfast", day)
        self.createSingleMealPanel("Lunch", day)
        self.createSingleMealPanel("Dinner", day)

    def createSingleMealPanel(self, meal, day):
        self.mealLabel = ttk.Label(self.dayFrame, text=meal, padding=(20,2,20,2))

        index = 0
        if meal == "Lunch":
            index = 1
        elif meal == "Dinner":
            index = 2

        self.mealLabel.grid(column=1, row=index)
        self.createSpecialOptionsDropdown(day)
        (self.dropdownDict[day][-1].display).grid(column=2, row=index)
    
    def createSpecialOptionsDropdown(self, day):
            super().createSpecialOptionsDropdown(self.dayFrame)
            self.dropdownDict[day].append(self.specialDropdown)
    
    def createSubmitButton(self):
        super().createSubmitButton()
        self.submitButton.grid(column=0, columnspan=3, row=1)

    def generatePlan(self):

        super().generatePlan()
        self.meal_creator.setWeeklyPreferencesAdvanced(self.dropdownDict)
        self.meal_creator.create_meal_plan()

        self.clearPage()
        displayMealPage = MealInfoDisplay(self.outer, self.meal_creator)




