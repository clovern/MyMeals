from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PlanPage import PlanPage
from MealFileSaver import MealFileSaver
from idlelib.tooltip import Hovertip
from MealDetailPopup import MealDetailPopup

class MealInfoDisplay(PlanPage):
    def __init__(self, outer, mealcreator):
        self.outer = outer
        self.meal_creator = mealcreator
        super().__init__()
        self.createMealDisplay()
    
    def createMealDisplay(self):
        self.create_lower_left_frame()
        self.create_lower_right_frame()
        self.lowercontent["height"] = 600
        self.create_title("You're all set!")
        self.create_all_days()
        self.create_footer_options()
    
    def create_day_panel(self, day, index):
        super().create_day_panel(day, index)
        self.day_frame['width'] = 400
        self.create_meal_display_panel("Breakfast", day)
        self.create_meal_display_panel("Lunch", day)
        self.create_meal_display_panel("Dinner", day)

    def create_meal_display_panel(self, meal, day):

        mealday = self.meal_creator.mealdays_dict[day]
        self.display_meal(mealday, meal)
    
    def display_meal(self, mealday, meal):

        text_value= self.set_meal_label(mealday, meal)
        index = self.set_meal_index(meal)

        meal_label = ttk.Label(self.day_frame, text=text_value, padding=(20,2,20,2), wraplength = 125)
        meal_label.grid(column=3, row=index, sticky='W')
        self.create_reroll_button(mealday, meal, meal_label)
        self.create_details_button(mealday, meal)

    def set_meal_label(self, mealday, meal):
        text_value = "B"
        if meal.lower() == "lunch":
            text_value = "L"
        elif meal.lower() == "dinner":
            text_value = "D"

        text_value += ": "
        meal_value = self.meal_creator.get_meal_selection(mealday, meal)
        if meal_value == "N/A":
            text_value += "No Meals Match Criteria"
        else:
            text_value += meal_value.__repr__()
        
        return text_value
    
    def create_details_button(self, mealday, meal):
        index = self.set_meal_index(meal)
        self.details_button = ttk.Button(self.day_frame, text=u"\U0001F441", width = 3, default="active", command=lambda: self.show_meal_details(mealday, meal))
        self.details_button.grid(row=index, column=2, sticky='E')
        details_tip = Hovertip(self.details_button, "Details")

    def create_reroll_button(self, mealday, meal, label):
        index = self.set_meal_index(meal)
        self.reroll_button = ttk.Button(self.day_frame, text="\u27f3", width = 3, default="active", command=lambda: self.reroll_meal(mealday, meal, label))
        self.reroll_button.grid(row=index, column=1, sticky='E')
        reroll_tip = Hovertip(self.reroll_button, "Re-Roll")

    def show_meal_details(self, mealday, meal):
        MealDetailPopup(mealday, meal)

    def reroll_meal(self, mealday, meal, label):
        self.meal_creator.select_meal(mealday, meal)
        self.update_meal_display(mealday, meal, label)
    
    def update_meal_display(self, mealday, meal, label):
        text_value = self.set_meal_label(mealday, meal)
        label["text"] = text_value

    def create_footer_options(self):
        self.save_button = ttk.Button(self.lowercontent, text="save to file", default="active", command=self.save_meals)
        self.save_button.grid(column=0, columnspan=3, row=1)

    def save_meals(self):

        meal_plan = self.meal_creator.mealdays_dict
        MealFileSaver.save_meal_plan(meal_plan)
