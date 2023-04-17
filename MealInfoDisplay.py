from tkinter import *
from tkinter import messagebox
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

        mealday = self.meal_creator.mealdays_dict[day]
        self.display_meal(mealday, meal)
        self.create_details_button()
    
    def display_meal(self, mealday, meal):

        text_value= self.set_meal_label(mealday, meal)
        index = self.set_meal_index(meal)

        meal_label = ttk.Label(self.day_frame, text=text_value, padding=(20,2,20,2))
        meal_label.grid(column=2, row=index)
        self.create_reroll_button(mealday, meal, meal_label)
    
    def set_meal_index(self, meal):
        index = 0
        if meal.lower() == "lunch":
            index = 1
        elif meal.lower() == "dinner":
            index = 2
        return index

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
    
    def create_details_button(self):
        self.details_button = ttk.Button(self.day_frame, text="details", default="active", command=self.show_meal_details)
        self.details_button.grid(row=3, column=0)

    def create_reroll_button(self, mealday, meal, label):
        # self.reroll_button = ttk.Button(self.day_frame, text="re-roll", default="active", command=self.reroll_meal(mealday, meal))
        index = self.set_meal_index(meal)
        self.reroll_button = ttk.Button(self.day_frame, text="Re-Roll", default="active", command=lambda: self.reroll_meal(mealday, meal, label))
        self.reroll_button.grid(row=index, column=1)

    def show_meal_details(self, meal):
        # open a message box that shows the ingredients and the recipe
        messagebox.showinfo("showinfo", "Information")
        pass

    def reroll_meal(self, mealday, meal, label):
        self.meal_creator.select_meal(mealday, meal)
        self.update_meal_display(mealday, meal, label)
    
    def update_meal_display(self, mealday, meal, label):
        text_value = self.set_meal_label(mealday, meal)
        label["text"] = text_value
        

    def create_footer_options(self):
        self.save_button = ttk.Button(self.footercontent, text="save to file", default="active", command=self.save_meals)
        self.save_button.pack()

    def save_meals(self):
        pass
