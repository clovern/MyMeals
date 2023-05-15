from tkinter import filedialog
import os
from datetime import date, timedelta
from Meal import Meal
from GUI.FileSaver import FileSaver

class MealFileSaver(FileSaver):

    def __init__(self):
        self.meal_text = "" 

    #meal_plan should be a dictionary of MealDays, as created in MealPlanCreator
    def generate_file_text(self, meal_plan):

        start_date = date.today()
        end_date = start_date + timedelta(days=7)

        self.meal_text +="Meal plan for " + str(start_date) + " - " + str(end_date)
        for day in meal_plan:
            mealday = meal_plan[day]

            self.meal_text +="\n\n"
            self.meal_text +="_____________________________________________________________________________________\n"
            self.meal_text +=mealday.day
            self.meal_text +=": \n\n"

            if isinstance(mealday.breakfast_choice, Meal):
                self.meal_text +="\n"
                self.meal_text +="Breakfast:\n"
                self.meal_text +="\n"
                self.write_meal_to_string(mealday.breakfast_choice)
            
            if isinstance(mealday.lunch_choice, Meal):
                self.meal_text +="\n"
                self.meal_text +=".   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .\n"
                self.meal_text +="Lunch:\n"
                self.meal_text +="\n"
                self.write_meal_to_string(mealday.lunch_choice)
            
            if isinstance(mealday.dinner_choice, Meal):
                self.meal_text +="\n"
                self.meal_text +=".   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .\n"
                self.meal_text +="Dinner:\n"
                self.meal_text +="\n"
                self.write_meal_to_string(mealday.dinner_choice)

        return self.meal_text
        
    def write_meal_to_string(self, meal):
        self.meal_text +=meal.name
        self.meal_text +="\n"
        ingredients = meal.format_meal_ingredients()
        self.meal_text +="\n" + ingredients
        recipe_or_link = meal.format_link_or_recipe_text()
        self.meal_text +="\n" + recipe_or_link
