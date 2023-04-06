from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from SpecialOptionsDropdown import SpecialOptionsDropdown
from MealCreator import MealCreator
from PlanPage import PlanPage

class MealInfoDisplay(PlanPage):
    def __init__(self, outer, mealcreator):
        self.outer = outer
        self.meal_creator = mealcreator
        super().__init__()
        self.createMealDisplay()
    
    def createMealDisplay(self):
        self.createLowerLeftFrame()
        self.createLowerRightFrame()
        self.createFooterFrame()
        self.lowercontent["height"] = 500
        self.createTitle("You're all set!")
        self.createAllDays()
        self.createFooterOptions()
    
    def createFooterFrame(self):
        self.footercontent = ttk.Frame(self.outer, height=100, width=800)
        self.footercontent.grid(column=0, row=2)
        self.footercontent.grid_propagate(0)
    
    def createDayPanel(self, day, index):
        super().createDayPanel(day, index)
        self.createMealDisplayPanel("Breakfast", day)
        self.createMealDisplayPanel("Lunch", day)
        self.createMealDisplayPanel("Dinner", day)

    def createMealDisplayPanel(self, meal, day):
        self.displayMeal(meal, day)
        self.createDetailsButton()
        self.createReRollButton()
    
    def displayMeal(self, meal, day):
        textValue = meal
        textValue += ": "
        textValue += self.meal_creator.get_meal_choice(day, meal).__repr__()
        self.mealLabel = ttk.Label(self.dayFrame, text=textValue, padding=(20,2,20,2))

        index = 0
        if meal == "Lunch":
            index = 1
        elif meal == "Dinner":
            index = 2

        self.mealLabel.grid(column=1, row=index)
    
    def createDetailsButton(self):
        self.detailsButton = ttk.Button(self.dayFrame, text="details", default="active", command=self.showMealDetails)
        self.detailsButton.grid(row=3, column=0)

    def createReRollButton(self):
        self.rerollButton = ttk.Button(self.dayFrame, text="re-roll", default="active", command=self.reRollMeal)
        self.rerollButton.grid(row=3, column=1)

    def showMealDetails(self):
        pass

    def reRollMeal(self):
        pass

    def createFooterOptions(self):
        self.saveButton = ttk.Button(self.footercontent, text="save to file", default="active", command=self.saveMeals)
        self.saveButton.pack()

    def saveMeals(self):
        pass
