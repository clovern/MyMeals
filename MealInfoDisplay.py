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
        self.createTitle("You're all set!")
        self.createAllDays()
    
    def createDayPanel(self, day, index):
        super().createDayPanel(day, index)
        self.createMealDisplayPanel("Breakfast", day)
        self.createMealDisplayPanel("Lunch", day)
        self.createMealDisplayPanel("Dinner", day)

    
    def createMealDisplayPanel(self, meal, day):
        textValue = meal
        textValue += " "
        textValue += self.meal_creator.get_meal_choice(day, meal).__repr__()
        self.mealLabel = ttk.Label(self.dayFrame, text=textValue, padding=(20,2,20,2))

        index = 0
        if meal == "Lunch":
            index = 1
        elif meal == "Dinner":
            index = 2

        self.mealLabel.grid(column=1, row=index)