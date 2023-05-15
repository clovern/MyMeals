from tkinter import *
from tkinter import ttk
from GUI.PlanPage import PlanPage
from GUI.MealInfoDisplay import MealInfoDisplay
from GUI.CustomDropdowns.DropdownTranslator import DropdownTranslator
from idlelib.tooltip import Hovertip
from GUI.CustomPopups.MealSearcherPopup import MealSearcherPopup

class AdvancedPlanPage(PlanPage):
    def __init__(self, root, outer, previous):
        self.root = root
        self.outer = outer
        self.previous = previous
        super().__init__()
        self.dropdown_dict = {"Monday": {"breakfast": None, "lunch": None, "dinner": None}, "Tuesday": {"breakfast": None, "lunch": None, "dinner": None}, "Wednesday": {"breakfast": None, "lunch": None, "dinner": None}, "Thursday": {"breakfast": None, "lunch": None, "dinner": None},
                        "Friday": {"breakfast": None, "lunch": None, "dinner": None}, "Saturday": {"breakfast": None, "lunch": None, "dinner": None}, "Sunday": {"breakfast": None, "lunch": None, "dinner": None}}
        self.chosen_meals_dict = {"Monday": {"breakfast": None, "lunch": None, "dinner": None}, "Tuesday": {"breakfast": None, "lunch": None, "dinner": None}, "Wednesday": {"breakfast": None, "lunch": None, "dinner": None}, "Thursday": {"breakfast": None, "lunch": None, "dinner": None},
                        "Friday": {"breakfast": None, "lunch": None, "dinner": None}, "Saturday": {"breakfast": None, "lunch": None, "dinner": None}, "Sunday": {"breakfast": None, "lunch": None, "dinner": None}}
        self.search_widgets = {"Monday": [[], [], []], "Tuesday": [[], [], []], "Wednesday": [[], [], []], "Thursday": [[], [], []],
                        "Friday": [[], [], []], "Saturday": [[], [], []], "Sunday": [[], [], []]}
        self.create_advanced_plan_display()
    
    def create_advanced_plan_display(self):
        self.create_lower_left_frame()
        self.create_lower_right_frame()
        self.create_back_button()
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
        self.create_meal_search_button(meal, day, self.day_frame)
        self.create_special_options_dropdown(day, meal, self.day_frame)
        (self.dropdown_dict[day][meal.lower()].display).grid(column=2, row=index)
    
    def create_meal_search_button(self, meal, day, frame):
        index = self.set_meal_index(meal)
        self.search_button = ttk.Button(self.day_frame, text=u"\U0001F50D", width = 3, command=lambda: self.search_meals(self, meal, day, frame))
        self.search_button.grid(row=index, column=3, sticky='W', padx = (5, 0))
        serach_tip = Hovertip(self.search_button, "Search for Meal by Name")
    
    def search_meals(self, advanced_plan_page, meal, day, frame):
        advanced_opts = {"meal" : meal,
                         "day" : day,
                         "frame": frame}
        self.meal_search = MealSearcherPopup(advanced_plan_page, advanced_opts)

    def update_meal_for_search(self, meal_selection):

        day = self.meal_search.day
        meal = self.meal_search.meal
        frame = self.meal_search.frame

        index = self.set_meal_index(meal)
        if self.dropdown_dict[day][meal.lower()] != None:
            self.dropdown_dict[day][meal.lower()].display.destroy()
        for widget in self.search_widgets[day][index]:
            widget.destroy()
        self.dropdown_dict[day][meal.lower()] = None
        self.chosen_meals_dict[day][meal.lower()] = meal_selection

        chosen_label = ttk.Label(frame, text = meal_selection.name.title(), wraplength=110)
        chosen_label.grid(column=2, row=index)
        self.search_widgets[day][index].append(chosen_label)
        self.delete_selected_meal_button(meal, day, frame, chosen_label)
    
    def delete_selected_meal_button(self, meal, day, frame, label):
        index = self.set_meal_index(meal)
        delete_selected_btn = ttk.Button(frame, text="\u2718", width = 3, command=lambda: self.restore_dropdown_menu(meal, day, frame))
        self.search_widgets[day][index].append(delete_selected_btn)
        delete_selected_btn.grid(row=index, column=5, sticky='W', padx = (5, 0))
        Hovertip(delete_selected_btn, "Delete Meal Selection")

    def restore_dropdown_menu(self, meal, day, frame):
        index = self.set_meal_index(meal)
        for widget in self.search_widgets[day][index]:
            widget.destroy()
        self.create_special_options_dropdown(day, meal, frame)
        self.dropdown_dict[day][meal.lower()] = self.special_dropdown
        (self.dropdown_dict[day][meal.lower()].display).grid(column=2, row=index)
        self.chosen_meals_dict[day][meal.lower()] = None

    def create_special_options_dropdown(self, day, meal, frame):
            super().create_special_options_dropdown(frame, "advanced")
            self.dropdown_dict[day][meal.lower()] = (self.special_dropdown)

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
        for day in self.dropdown_dict:
            self.dropdown_dict[day][meal.lower()].set_exclude()
    
    def create_submit_button(self):
        super().create_submit_button()
        self.submit_button.grid(column=0, columnspan=3, row=1)

    def generate_plan(self):

        super().generate_plan()
        dropdown_translator = DropdownTranslator()
        weekly_preferences = dropdown_translator.set_weekly_preferences_advanced(self.dropdown_dict, self.chosen_meals_dict)
        self.meal_creator.create_meal_plan(weekly_preferences)
        self.meal_creator.set_chosen_meals(self.chosen_meals_dict)

        self.clear_page()
        display_meal_page = MealInfoDisplay(self.root, self.outer, self.meal_creator, self.content)


