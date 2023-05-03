from tkinter import *
from tkinter import ttk
from PlanPage import PlanPage
from idlelib.tooltip import Hovertip

class MealListDisplay(PlanPage):

    def __init__(self, outer, previous):
        self.outer = outer
        self.previous = previous
        super().__init__()
        # self.headercontent, self.uppercontent, self.lowercontent created
        self.createMealDisplay()
    
    def createMealDisplay(self):
        self.lowercontent["height"] = 600
        self.create_title("Meal List")
        self.create_back_button()