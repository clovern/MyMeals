from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from PlanPage import PlanPage

class AdvancedPlanPage(PlanPage):
    def __init__(self, root, outer):
        self.outer = outer
        self.dropdownDict = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [],
                        "Friday": [], "Saturday": [], "Sunday": []}
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
        self.createSingleMealPanel("Breakfast", day)
        self.createSingleMealPanel("Lunch", day)
        self.createSingleMealPanel("Dinner", day)

    def createDayFlag(self, day):
        self.dayFlag = ttk.Label(self.dayFrame, text=day, width=10, font=("Arial", 15))
        self.dayFlag.grid(column=0, row=0)

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

        print("________________________________")
        print(self.dropdownDict["Monday"][0].veganBool.get())
        print("________________________________")
        super().generatePlan()
        self.meal_creator.set_mealday_preference("Monday", "dinner", {'meat_type': 'vegan'})

        # need to add preferences for every meal and every day
        # the days would be keys in the dict
        # each day will have 3 values (0, 1, and 2) corresponding to breakfast lunch and dinner
        # for day in self.dropdownDict.keys():
        #     self.dropdownDict["Monday"][-1].get()

        self.meal_creator.create_meal_plan()

        self.meal_creator.print_meals()




