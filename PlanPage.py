from tkinter import *
from tkinter import ttk
from SpecialOptionsDropdown import SpecialOptionsDropdown
from MealCreator import MealCreator
from Page import Page

class PlanPage(Page):
    def __init__(self):
        self.createUpperFrame()
        self.createLowerFrame()
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def createSubmitButton(self):
        self.submitButton = ttk.Button(self.lowercontent, text="Create Plan", default="active", command=self.generatePlan)

    def createSpecialOptionsDropdown(self, frame):
        self.specialDropdown = SpecialOptionsDropdown(frame)

    def generatePlan(self):
        self.meal_creator = MealCreator()
        self.weeklyPreferences = {"Monday": [{}, {}, {}], "Tuesday": [{}, {}, {}], "Wednesday": [{}, {}, {}], "Thursday": [{}, {}, {}],
                        "Friday": [{}, {}, {}], "Saturday": [{}, {}, {}], "Sunday": [{}, {}, {}]}
    
    def createAllDays(self):
        index = 0
        for day in self.days:
            self.createDayPanel(day, index)
            index += 1
    
    def createDayFlag(self, day):
        self.dayFlag = ttk.Label(self.dayFrame, text=day, width=10, font=("Arial", 15))
        self.dayFlag.grid(column=0, row=0)
    
    def createDayPanel(self, day, index):
        if (index < 4):
            self.dayFrame= ttk.Frame(self.lowerLeftContent)
        else:
            self.dayFrame= ttk.Frame(self.lowerRightContent)
            index -= 4
        
        self.dayFrame['padding'] = (10, 10, 10, 10)
        self.dayFrame.grid(column=0, row=index)
        self.createDayFlag(day)
    
    def getSelection(self, dropdown): 
        selectedInitial = []
        selectedFinal = {}
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