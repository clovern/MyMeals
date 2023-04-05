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

        self.weeklyPreferences = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [],
                        "Friday": [], "Saturday": [], "Sunday": []}

        super().generatePlan()

        #add selected options from each day to weeklyPreferences, as an array
        for day in self.days:
            for index in range(3):
                self.weeklyPreferences[day].append(self.getSelection(day, index))

        self.setDailyPreferences(self.weeklyPreferences)

        self.meal_creator.create_meal_plan()

        self.meal_creator.print_meals()

        self.clearPage()
        displayMealPage = MealInfoDisplay(self.outer, self.meal_creator)

    
    def getSelection(self, day, index): 
        selectedInitial = []
        selectedFinal = {}
        dropdown = self.dropdownDict[day][index]
        dropdownOptions = dropdown.dropdownVars

        # adds all selected values directly into selectedInitial list
        for i in range(len(dropdownOptions)):

            #value of 1 indicates this variable is selected
            if dropdownOptions[i].get() == 1:
                selectedOption = dropdown.dropdownOpts[i]
                selectedInitial.append(selectedOption)
        
        selectedFinal = self.formatSelection(selectedInitial)
                
        return selectedFinal

    def formatSelection(self, selectedInitial):
        
        selectedFinal = {}
        # If multiple values are selected for meat type or price, these selections are put into arrays.
        # This allows us to search for meals which match 1 or more of these options in MealCreator. 
        meat_types = []
        price_types = []
        for value in selectedInitial:
            if value.lower() in ["vegan", "vegetarian", "chicken", "pork", "beef", "turkey", "seafood"]:
                meat_types.append(value.lower())
            elif value in ["$", "$$", "$$$"]:
                if (value == "$"):
                    price_types.append("cheap")
                elif (value == "$$"):
                    price_types.append("medium")
                elif (value == "$$$"):
                    price_types.append("expensive")
            else:
                if (value.lower() == "reheats-well"):
                    selectedFinal["reheats_well"] = "true"

        if (len(meat_types) > 0):
            if (len(meat_types) == 1):
                selectedFinal["meat_type"] = meat_types[0]
            else:
                selectedFinal["meat_type"] = meat_types
        
        if (len(price_types) > 0):
            if (len(meat_types) == 1):
                selectedFinal["price_range"] = price_types[0]
            else:
                selectedFinal["price_range"] = price_types
                
        return selectedFinal
    
    def setDailyPreferences(self, weeklyPreferences):
        breakfastindex = 0
        lunchindex = 1
        dinnerindex = 2

        for day in self.days:

            self.meal_creator.set_mealday_preference(day, "breakfast", weeklyPreferences[day][breakfastindex])
            self.meal_creator.set_mealday_preference(day, "lunch", weeklyPreferences[day][lunchindex])
            self.meal_creator.set_mealday_preference(day, "dinner", weeklyPreferences[day][dinnerindex])
            
        return




