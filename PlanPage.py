from tkinter import *
from tkinter import ttk
from SpecialOptionsDropdown import SpecialOptionsDropdown
from MealCreator import MealCreator
from Page import Page

class PlanPage(Page):
    def __init__(self):
        self.create_upper_frame()
        self.create_lower_frame()
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def create_submit_button(self):
        self.submit_button = ttk.Button(self.lowercontent, padding = 3, text="Create Plan", default="active", command=self.generate_plan)

    def create_special_options_dropdown(self, frame, type):
        self.special_dropdown = SpecialOptionsDropdown(frame, type)

    def generate_plan(self):
        self.meal_creator = MealCreator()
    
    def create_all_days(self):
        index = 0
        for day in self.days:
            self.create_day_panel(day, index)
            index += 1
    
    def create_day_flag(self, day):
        self.dayFlag = ttk.Label(self.day_frame, text=day, width=10, font=("Arial", 15))
        self.dayFlag.grid(column=0, row=0)
    
    def set_meal_index(self, meal):
        index = 0
        if "lunch" in meal.lower():
            index = 1
        elif "dinner" in meal.lower():
            index = 2
        return index
    
    def create_day_panel(self, day, index):
        if (index < 4):
            self.day_frame= ttk.Frame(self.lower_left_content)
        else:
            self.day_frame= ttk.Frame(self.lower_right_content)
            index -= 4

        self.day_frame['padding'] = (10, 10, 10, 10)
        self.day_frame.grid(column=0, row=index, sticky='W')
        self.create_day_flag(day)