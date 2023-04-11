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
        self.dropdown_dict = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [],
                        "Friday": [], "Saturday": [], "Sunday": []}
        self.create_advanced_plan_display()
    
    def create_advanced_plan_display(self):
        self.create_lower_left_frame()
        self.create_lower_right_frame()
        self.create_title("Advanced Plan Creator")
        self.create_all_days()
        self.create_submit_button()

    def create_day_panel(self, day, index):
        super().create_day_panel(day, index)
        self.create_single_meal_panel("Breakfast", day)
        self.create_single_meal_panel("Lunch", day)
        self.create_single_meal_panel("Dinner", day)

    def create_single_meal_panel(self, meal, day):
        self.meal_label = ttk.Label(self.day_frame, text=meal, padding=(20,2,20,2))

        index = 0
        if meal == "Lunch":
            index = 1
        elif meal == "Dinner":
            index = 2

        self.meal_label.grid(column=1, row=index)
        self.create_special_options_dropdown(day)
        (self.dropdown_dict[day][-1].display).grid(column=2, row=index)
    
    def create_special_options_dropdown(self, day):
            super().create_special_options_dropdown(self.day_frame)
            self.special_dropdown.make_advanced()
            self.dropdown_dict[day].append(self.special_dropdown)
    
    def create_submit_button(self):
        super().create_submit_button()
        self.submit_button.grid(column=0, columnspan=3, row=1)

    def generate_plan(self):

        super().generate_plan()
        self.meal_creator.set_weekly_preferences_advanced(self.dropdown_dict)
        self.meal_creator.create_meal_plan()

        self.clear_page()
        display_meal_page = MealInfoDisplay(self.outer, self.meal_creator)




