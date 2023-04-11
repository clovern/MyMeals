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
        self.create_lower_left_frame()
        self.create_lower_right_frame()
        self.create_footer_frame()
        self.lowercontent["height"] = 500
        self.create_title("You're all set!")
        self.create_all_days()
        self.create_footer_options()
    
    def create_footer_frame(self):
        self.footercontent = ttk.Frame(self.outer, height=100, width=800)
        self.footercontent.grid(column=0, row=2)
        self.footercontent.grid_propagate(0)
    
    def create_day_panel(self, day, index):
        super().create_day_panel(day, index)
        self.create_meal_display_panel("Breakfast", day)
        self.create_meal_display_panel("Lunch", day)
        self.create_meal_display_panel("Dinner", day)

    def create_meal_display_panel(self, meal, day):
        self.display_meal(meal, day)
        self.create_details_button()
        self.create_reroll_button()
    
    def display_meal(self, meal, day):
        text_value = meal
        text_value += ": "
        text_value += self.meal_creator.get_meal_selection(day, meal).__repr__()
        self.meal_label = ttk.Label(self.day_frame, text=text_value, padding=(20,2,20,2))

        index = 0
        if meal == "Lunch":
            index = 1
        elif meal == "Dinner":
            index = 2

        self.meal_label.grid(column=1, row=index)
    
    def create_details_button(self):
        self.details_button = ttk.Button(self.day_frame, text="details", default="active", command=self.show_meal_details)
        self.details_button.grid(row=3, column=0)

    def create_reroll_button(self):
        self.reroll_button = ttk.Button(self.day_frame, text="re-roll", default="active", command=self.reroll_meal)
        self.reroll_button.grid(row=3, column=1)

    def show_meal_details(self):
        pass

    def reroll_meal(self):
        pass

    def create_footer_options(self):
        self.save_button = ttk.Button(self.footercontent, text="save to file", default="active", command=self.save_meals)
        self.save_button.pack()

    def save_meals(self):
        pass
