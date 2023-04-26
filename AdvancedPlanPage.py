from tkinter import *
from tkinter import ttk
from PlanPage import PlanPage
from MealInfoDisplay import MealInfoDisplay
from DropdownTranslator import DropdownTranslator
from idlelib.tooltip import Hovertip
from MealSearcherPopup import MealSearcherPopup

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
        self.create_quick_exclude_options()
        self.create_submit_button()

    def create_day_panel(self, day, index):
        super().create_day_panel(day, index)
        self.create_single_meal_panel("Breakfast", day)
        self.create_single_meal_panel("Lunch", day)
        self.create_single_meal_panel("Dinner", day)

    def create_single_meal_panel(self, meal, day):
        self.meal_label = ttk.Label(self.day_frame, text=meal, padding=(20,2,20,2))

        index = self.set_meal_index(meal)

        self.meal_label.grid(column=1, row=index)
        self.create_meal_search_button(index)
        self.create_special_options_dropdown(day)
        (self.dropdown_dict[day][-1].display).grid(column=2, row=index)
    
    def create_meal_search_button(self, index):
        self.search_button = ttk.Button(self.day_frame, text=u"\U0001F50D", width = 3, command=lambda: self.search_meals())
        self.search_button.grid(row=index, column=3, sticky='W', padx = (5, 0))
        serach_tip = Hovertip(self.search_button, "Search for Meal by Name")
    
    def search_meals(self):
        MealSearcherPopup()
    
    def create_special_options_dropdown(self, day):
            super().create_special_options_dropdown(self.day_frame, "advanced")
            self.dropdown_dict[day].append(self.special_dropdown)

    def create_quick_exclude_options(self):
        self.lower_options_frame= ttk.Frame(self.lower_left_content)
        self.lower_options_frame.grid(column=0, row=5, sticky='W')
        self.create_quick_exclude_button("breakfast")
        self.create_quick_exclude_button("lunch")
        self.create_quick_exclude_button("dinner")
    
    def create_quick_exclude_button(self, meal):
        index = self.set_meal_index(meal)
        text = "Exclude all "
        if meal == "breakfast" or meal == "dinner":
            text += meal.title() + 's'
        else: 
            text += meal.title() + "es"
        self.exclude_button = ttk.Button(self.lower_options_frame, text=text, default="active", width = 20, padding = 3, command=lambda: self.exclude_all(meal))
        self.exclude_button.grid(column = 0, row = index, padx = (17, 0), pady=(10,0))
    
    def exclude_all(self, meal):
        index = self.set_meal_index(meal)
        for day in self.dropdown_dict:
            self.dropdown_dict[day][index].set_exclude()
    
    def create_submit_button(self):
        super().create_submit_button()
        self.submit_button.grid(column=0, columnspan=3, row=1)

    def generate_plan(self):

        super().generate_plan()
        dropdown_translator = DropdownTranslator()
        weekly_preferences = dropdown_translator.set_weekly_preferences_advanced(self.dropdown_dict)
        self.meal_creator.create_meal_plan(weekly_preferences)

        self.clear_page()
        display_meal_page = MealInfoDisplay(self.outer, self.meal_creator)




